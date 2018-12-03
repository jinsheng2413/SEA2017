# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: data_access.py
@time: 2018/5/23 0023 14:04
@desc:测试数据提取的数据库访问类
"""

import os

from com.nrtest.common.dictionary import Dict
from com.nrtest.common.ora_drv import PyOracle
from com.nrtest.common.setting import Setting

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# 或者os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'

class DataAccess:

    @staticmethod
    def getMenu(menuNo, by_name=False):

        pyoracle = PyOracle.getInstance()
        fun_name = 'pkg_nrtest.get_menu_path' + ('_by_name' if by_name else '')
        menu_path = pyoracle.callfunc(fun_name, 'str', [menuNo])
        return menu_path

    @staticmethod
    def getAllMenu():
        """
        获取测试系统所有菜单
        :return:
        """

        pyoracle = PyOracle.getInstance()
        cur = pyoracle.callFCur('pkg_nrtest.get_all_menu', [Setting.DEFAULT_USER])
        return cur

    @staticmethod
    def getLeftTree(treeNO):
        pyoracle = PyOracle.getInstance()
        org_path = pyoracle.callfunc('pkg_nrtest.get_org_path', 'str', [treeNO])
        return org_path

    @staticmethod
    def getCaseData(menuNo, tabName='', groupNo='', valCheck=False):
        """
        根据菜单编号提取测试用例数据
        :param menuNo: 菜单编号
        :param tabName: Tab页名
        :param groupNo: 用例组编号
        :param valCheck: True-对元素数据有效性校验；False-测试用例数据
        :return: 返回用例数据
        """
        pyoracle = PyOracle.getInstance()
        qry = [Setting.GROUP_USER, menuNo, groupNo, tabName]

        # funName = 'pkg_nrtest.get_tst_case_for_valid' if valCheck else 'pkg_nrtest.get_tst_case'
        # tst_case = pyoracle.callfunc(funName, 'str', qry)

        funName = 'pkg_nrtest.get_tst_case_for_valid_cur' if valCheck else 'pkg_nrtest.get_tst_case_cur'
        tst_case = pyoracle.callFCur(funName, qry)
        print(tst_case)
        try:
            rslt = []
            for row in tst_case:
                rslt.append(Dict(eval(row[0])))
            if len(rslt) == 0:
                print(
                    '没有user_group：{} 与菜单编号：{} 的测试用例数据'.format(qry[0], qry[1]))
            print('当前用例数据：\n', rslt, '\n')
        except BaseException:
            print('获取测试用例数据失败，请检查用例用户组名称是否配置正确，用例编写是否符合要求')
        return rslt

    @staticmethod
    def refresh_case(user_no='', group_no=''):
        """
        用于默认刷新admin用户下的‘00000’用户组的测试用例
        :param user_no: 测试用例用户
        :param group_no: 测试用例组
        :return:
        """
        para = [Setting.GROUP_USER if user_no == '' else user_no,
                '00000' if group_no == '' else group_no]
        pyoracle = PyOracle.getInstance()
        cases = pyoracle.callproc('pkg_nrtest.refresh_case', para)

        return cases

    @staticmethod
    def get_case_result(tst_case_id):
        """
        用于默认刷新admin用户下的‘00000’用户组的测试用例
        :param user_no: 测试用例用户
        :param group_no: 测试用例组
        :return:
        """
        sql = 'select assert_type,tab_column_name , column_name, expected_value from tst_case_result where tst_case_id = :id order by assert_type'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [tst_case_id])
        return dataSet

    @staticmethod
    def refresh_menu(p_menu_no=''):
        """
        刷新菜单关系（由坐标定位改为按名称定位）
        :param p_menu_no: 父节点菜单编码，该值为空刷新全部菜单，否则刷新指定菜单
        """
        pyoracle = PyOracle.getInstance()
        if p_menu_no == '':
            pyoracle.callproc('pkg_nrtest.refresh_menu')
        else:
            para = [p_menu_no]
            pyoracle.callproc('pkg_nrtest.refresh_menu', para)

    @staticmethod
    def refresh_menu_xapth(menu_no=''):
        """
        用例数据填完后，刷新菜单/TAB对应的元素清单
        :param menu_no: 菜单编码，该值为空刷新全部菜单，否则刷新指定菜单
        """
        pyoracle = PyOracle.getInstance()
        pyoracle.callproc('pkg_nrtest.refresh_menu_xapth', [menu_no])


if __name__ == '__main__':
    # DataAccess.refresh_case()
    print(DataAccess.getCaseData("99942110"))
    # print(type(str))
    # print(DataAccess.get_case_result('999111003'))
    # val = Dict(eval(str[4]['ORG_NO']))
    # print(val['FLAG'], val['VALUE'])

    # for i in  str[4:10]:
    #     print(i)
    # print(DataAccess.getAllMenu())
    # DataAccess.getMenu('99913210')
    # pass
    # 刷新菜单/tab对应的元素
    # DataAccess.refresh_menu_xapth('填写要刷新的菜单编号')
    # DataAccess.get_case_result('999111003')
