# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: data_access.py
@time: 2018/5/23 0023 14:04
@desc:测试数据提取的数据库访问类
'''

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

        pyoracle = PyOracle.getInstance()
        cur = pyoracle.callFCur('pkg_nrtest.get_all_menu')

        return cur

    @staticmethod
    def getLeftTree(treeNO):
        pyoracle = PyOracle.getInstance()
        org_path = pyoracle.callfunc('pkg_nrtest.get_org_path', 'str', [treeNO])
        return org_path

    @staticmethod
    def getCaseData(menuNo, tabName='', groupNo=''):
        pyoracle = PyOracle.getInstance()
        qry = [Setting.GROUP_USER, menuNo, groupNo, tabName]
        tst_case = pyoracle.callfunc('pkg_nrtest.get_tst_case', 'str', qry)

        # 字符串转list
        rslt = eval(tst_case)
        if len(rslt) == 0:
            print('请确认以下配置项是否正确：\n1,配置文件（nari_test.conf）的user_group项：%s \n2,菜单编号：%s' % tuple(qry))
        print('当前用例数据：\n', rslt, '\n')

        # dict转Dict ljf
        for i in range(len(rslt)):
            rslt[i] = Dict(rslt[i])
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
    def reflash_menu(p_menu_no=''):
        """
        刷新菜单关系（由坐标定位改为按名称定位）
        :param p_menu_no: 父节点菜单编码，该值为空刷新全部菜单，否则刷新指定菜单
        """
        pyoracle = PyOracle.getInstance()
        if p_menu_no == '':
            pyoracle.callproc('pkg_nrtest.refresh_case')
        else:
            para = [p_menu_no]
            pyoracle.callproc('pkg_nrtest.refresh_case', para)


if __name__ == '__main__':
    # DataAccess.refresh_case()
    # str = DataAccess.getCaseData("99912100",tabName='终端调试')
    # print(len(str))
    # for i in  str[4:10]:
    #     print(i)
    print(DataAccess.getAllMenu())

    # DataAccess.getMenu('99913210')
