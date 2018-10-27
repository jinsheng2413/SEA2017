# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: oracle_test.py
@time: 2018/5/23 0023 14:04
@desc:
1.方法名：queryAll
        说明：查询表所有数据
        :param sql: sql语句
        :return: 返回所有查询数据
'''
import os

import cx_Oracle

from com.nrtest.common.setting import Setting

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# 或者os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'

class Oracle:
    """  oracle db operator  """

    def __init__(self, username=Setting.DB_USER, pwd=Setting.DB_PASSWORD, host=Setting.DB_HOST, name=Setting.DB_NAME):
        """

        :param userName: 用户名
        :param password: 密码
        :param host: ip
        :param instance: 数据库名称
        """
        self._conn = cx_Oracle.connect("%s/%s@%s/%s" % (username, pwd, host, name))
        self.cursor = self._conn.cursor()

    def queryAll(self, sql, para):
        """
        方法名：queryAll
        说明：查询表所有数据
        :param sql: sql语句
        :return: 返回所有查询数据
        """
        self.cursor.execute(sql, para)
        return self.cursor.fetchall()

    def queryOne(self, sql):
        """
        方法名：queryOne
        说明：查询一条数据

        :param sql: sql语句
        :return: 返回所有查询数据
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()


# print(lis)
# import unittest, ddt
#
# p = Oracle()
# lis = p.queryAll("SELECT t.LINE1 us,t.LINE2 FROM AU t where t.USECASENAME ")
#
# print(lis[0][1])
#
#
# @ddt.ddt
# class TestDtt(unittest.TestCase):
#
#
#     def setUp(cls):
#
#         print(u'开始测试---------------')
#
#
#
#
#     @ddt.data(*lis)
#     def test(self, data):
#         print(data[0], data[1])
#
#
#
#     @classmethod
#     def tearDownClass(cls):
#         print(u'结束测试------------------')
#

# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    p = Oracle()
    named_params = 'test_terminal_date_qry'

    fy = {'case_name': 'test_a_first_new_add', 'po': '分类名称'}
    p.cursor.execute(
        """select t.value_one,t.value_two from TEST_CASE t where  t.case_name =:case_name and t.value_one_name=:po""",
        fy)
    a = p.cursor.fetchall()
    print(a[0][0])
