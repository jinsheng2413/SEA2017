# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: mysaql.py
@time: 2018/12/18 0018 10:53
@desc:
"""
from com.nrtest.common.db_driver import PyOracle


# p = PyOracle()
# query = p.query('select tc.*,tc.rowid from tst_case tc where tc.menu_no =:menuNO and tc.tab_name =:tabName',['99913240','实时采集失败明细'])
# print(query)


def readData(menuNo, tabNmae='', name=''):
    p = PyOracle()
    if tabNmae != '':
        sql = 'select tst_case_id from tst_case tc where tc.menu_no =:menuNo and tc.tab_name =:tabName'
        res = p.query(sql, [menuNo, tabNmae])
    else:
        sql = 'select tst_case_id from tst_case tc where tc.menu_no =:menuNo'
        res = p.query(sql, [menuNo])

    # 插入11有值校验
    sql2 = 'insert into tst_case_result t (t.tst_case_id,t.assert_type,t.tab_column_name) values (:id,:type,:name)'

    for item in res:
        h = ''.join(item)
        print('--------')
        p.insert(sql2, [h, '11', name])
    # 修改tst_menu的 flag 值
    modifyData(menuNo)


def insertTable(*args):
    p = PyOracle()
    query = 'insert into tst_case_result  tr (tr.tst_case_id,tr.assert_type,tr.column_name,expected_value,tab_column_name) value(%s,%s,%s,%s,%s)'
    p.query(query % args)


def lineInsert(*agrs):
    for item in agrs:
        insertTable(item)


def modifyData(menuNo):
    sql = "update tst_menu ty set ty.flag =:flagNo where ty.menu_no =:menuNo"
    p = PyOracle()
    p.update(sql, ['09', menuNo])
    sql2 = "select t.remark,t.menu_no from tst_menu_xpath_list t where t.menu_no =:menuNo"
    sql3 = "update tst_menu_xpath_list tm set tm.use_share_xpath =:usef where tm.menu_no=:menuNo and tm.remark=:rmark"
    res = p.query(sql2, [menuNo])
    print(res)
    tab = 0
    tab2 = 0
    tab3 = 0
    for item in res:
        if item[0] == '03' and tab == 0:
            p.update(sql3, ['03', menuNo, '03'])
            tab = 1
        elif item[0] == '02' and tab2 == 0:
            p.update(sql3, ['02', menuNo, '02'])
            tab2 = 2
        elif item[0] == '00' and tab3 == 0:
            p.update(sql3, ['01', menuNo, '00'])
            tab3 = 3


# 没有tab页
readData('99952500', name='升级人员')
# 有tab页
# readData('99951100',tabNmae='',name= '部门')
# readData('99952200',name= '供电单位')
# 有tab页
readData('99952200', tabNmae='系统基本参数设置', name='上限值')
