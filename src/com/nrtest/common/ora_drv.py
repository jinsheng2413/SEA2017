# -*- coding:utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: ora_drv.py
@time: 2018-09-10 11:14
@desc:
"""
import datetime
import os

import cx_Oracle
from DBUtils.PooledDB import PooledDB

from com.nrtest.common.parse_nrtest import ParseNrTest


class ConnPool():
    """
    Oracle数据库连接池
    """
    __pool = None

    def __enter__(self):
        self.conn = self.__getConn()
        self.cursor = self.conn.cursor()
        print(u"数据库创建con和cursor")
        return self

    def __getConn(self):
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        # 或者os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'
        if self.__pool is None:
            parse = ParseNrTest()
            user = parse.get("Db_setup", "user_name")
            pwd = parse.get("Db_setup", "password")
            ip = parse.get("Db_setup", "IP")
            db = parse.get("Db_setup", "SID")
            maxcache = int(parse.get("Db_setup", "Maxcached"))

            dsn = ip + "/" + db
            self.__pool = PooledDB(creator=cx_Oracle, mincached=1, maxcached=maxcache,
                                   user=user, password=pwd,
                                   dsn=dsn)
        return self.__pool.connection()

    def __exit__(self, type, value, trace):
        """
        释放连接池资源
        """
        self.cursor.close()
        self.conn.close()
        print(u"PT连接池释放con和cursor")

    # 重连接池中取出一个连接
    def getconn(self):
        conn = self.__getConn()
        cursor = conn.cursor()
        return cursor, conn


class PyOracle():
    pyOracle = None

    def __init__(self):
        self._pool = ConnPool()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'inst'):
            cls.inst = super(PyOracle, cls).__new__(cls, *args, **kwargs)
        return cls.inst

    @classmethod
    def getInstance(cls):
        if PyOracle.pyOracle is None:
            PyOracle.pyOracle = PyOracle()
        return PyOracle.pyOracle

    def _close(self, cursor, conn):
        cursor.close()
        conn.close()

    # 查询
    def query(self, sql='', para=(), isAll=True):
        dataSet = None
        try:
            cursor, conn = self._pool.getconn()
            l = para is None if 0 else len(para)
            if l > 0:
                cursor.executemany(sql, para)
            else:
                cursor.execute(sql)

            if isAll:
                dataSet = cursor.fetchall()
            else:
                dataSet = cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self._close(cursor, conn)
        return dataSet

    # 增加
    def insert(self, sql='', para=()):
        return self._execute(sql, para)

    # 增加多行
    def insertMany(self, sql='', para=()):
        return self._executeMany(sql, para)

    # 更新
    def update(self, sql='', para=()):
        return self._execute(sql, para)

    # 删除
    def delete(self, sql='', para=()):
        return self._execute(sql, para)

    def deleteMany(self, sql='', para=()):
        return self._executeMany(sql, para)

    # """
    # DataAccess							cx_Oracle				Python
    # VARCHAR2, NVARCHAR2, LONG		cx_Oracle.STRING		str
    # CHAR							cx_Oracle.FIXED_CHAR	str
    # NUMBER							cx_Oracle.NUMBER		int
    # FLOAT							cx_Oracle.NUMBER		float
    # DATE							cx_Oracle.DATETIME		datetime.datetime
    # TIMESTAMP						cx_Oracle.TIMESTAMP		datetime.datetime
    # CLOB							cx_Oracle.CLOB			cx_Oracle.LOB
    # BLOB							cx_Oracle.BLOB			cx_Oracle.LOB
    # """

    def _pytype2ora(self, to_type):
        if to_type == 'str':
            cx_type = cx_Oracle.STRING
        elif to_type in ('int', 'float'):
            cx_type = cx_Oracle.NUMBER
        elif to_type in ('date', 'datetime', 'date2str', 'dt2str'):
            cx_type = cx_Oracle.DATETIME
        else:
            cx_type = cx_Oracle.STRING
        return cx_type

    def callfunc(self, fun, retType='str', para=()):
        """
            调用Oracle函数
        :param fun: 要调用的oracle函数名
        :param para: 调用参数
        :param retType: Oracle函数返回数据类型
                        int：整型,不带小数点
                        float:浮点小数
                        date：日期
                        datetime：时间
                        date2str：日期转字符串
                        dt2str:   时间转字符串
        :return:
        """
        try:
            cursor, conn = self._pool.getconn()
            tp = cursor.var(self._pytype2ora(retType))
            rst = cursor.callfunc(fun, tp, para)
            if retType == 'int':
                rst = int(rst)
            elif retType == 'date':
                rst = datetime.datetime.strptime(rst.strftime('%Y-%m-%d'), '%Y-%m-%d')
            elif retType == 'date2str':
                rst = rst.strftime('%Y-%m-%d')
            elif retType == 'dt2str':
                rst = rst.strftime('%Y-%m-%d %H:%M:%S')
            conn.commit()
        except Exception as e:
            print('callfun   ', e, para)
            rst = None
            conn.rollback()
        finally:
            self._close(cursor, conn)
        return rst

    def callproc(self, proc, para=()):
        """
            调用Oracle Procedure
        :param proc: 要调用的oracle函数名
        :param para: 调用参数
        """
        try:
            cursor, conn = self._pool.getconn()
            cursor.callproc(proc, para)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            self._close(cursor, conn)

    def callPCur(self, proc, para=()):
        try:
            cursor, conn = self._pool.getconn()
            l_cur = cursor.var(cx_Oracle.CURSOR)
            para.append(l_cur)
            cursor.callproc(proc, para)
            rst = l_cur.getvalue().fetchall()
        except Exception as e:
            print('call proc for Cursor ', e)
            rst = None
        finally:
            self._close(cursor, conn)
        return rst

    def callFCur(self, fun, para=()):
        try:
            cursor, conn = self._pool.getconn()
            l_cur = cursor.var(cx_Oracle.CURSOR)
            cursor.callfunc(fun, l_cur, para)
            rst = l_cur.getvalue().fetchall()
        except Exception as e:
            print('call fun for Cursor ', e, e.args)
            rst = None
        finally:
            self._close(cursor, conn)
        return rst

    # 执行命令
    def _execute(self, sql='', para=()):
        res = False
        try:
            cursor, conn = self._pool.getconn()
            l = para is None if 0 else len(para)
            if l > 0:
                cursor.execute(sql, para)
            else:
                cursor.execute(sql)
            conn.commit()
            res = True
        except Exception as e:
            print(e)
            print(sql)
            print(para)
            conn.rollback()
        finally:
            self._close(cursor, conn)
        return res

    def _executeMany(self, sql='', para=[]):
        res = False
        try:
            cursor, conn = self._pool.getconn()
            cursor.executemany(sql, para)
            conn.commit()
            res = True
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            self._close(cursor, conn)
        return res

    def _executeManySql(self, ls=[]):
        """
        执行多条SQL
        :param ls: 参数格式 '[{"sql":"xxx","para":"xx"}....]'
        :return:
        """
        res = False
        try:
            cursor, conn = self._pool.getconn()
            for order in ls:
                sql = order['sql']
                para = order['para']
                if para:
                    cursor.execute(sql, para)
                else:
                    cursor.execute(sql)
            conn.commit()
            res = True
        except Exception as e:
            print('execute failed========', e)
            conn.rollback()
        finally:
            self._close(cursor, conn)
        return res
