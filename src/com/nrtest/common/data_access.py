# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: data_access.py
@time: 2018/5/23 0023 14:04
@desc:
1.方法名：queryAll
        说明：查询表所有数据
        :param sql: sql语句
        :return: 返回所有查询数据
'''
import cx_Oracle

from com.nrtest.common.dictionary import Dict
from com.nrtest.common.ora_drv import PyOracle
from com.nrtest.common.setting import Setting

import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# 或者os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'


class DataAccess:

    def getMenu(self, menuNo):

        pyoracle = PyOracle.getInstance()
        str = pyoracle.callfunc('pkg_nrtest.get_menu_path', 'str', [menuNo])

        return str

    def getLeftTree(self, treeNO):
        pyoracle = PyOracle.getInstance()
        str = pyoracle.callfunc('pkg_nrtest.get_org_path', 'str', [treeNO])
        return str

    def getCaseData(self, menuNo):
        pyoracle = PyOracle.getInstance()
        str = pyoracle.callfunc('pkg_nrtest.get_tst_case', 'str', [Setting.GROUP_USER, menuNo])

        return eval(str)
if __name__=='__main__':
    da =DataAccess()
    str =da.getMenu('99922120')
    print(str)


