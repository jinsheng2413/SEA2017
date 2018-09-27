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
    @staticmethod
    def getMenu(menuNo):

        pyoracle = PyOracle.getInstance()
        str = pyoracle.callfunc('pkg_nrtest.get_menu_path', 'str', [menuNo])

        return str
    @staticmethod
    def getLeftTree(treeNO):
        pyoracle = PyOracle.getInstance()
        str = pyoracle.callfunc('pkg_nrtest.get_org_path', 'str', [treeNO])
        return str
    @staticmethod
    def getCaseData(menuNo):
        pyoracle = PyOracle.getInstance()
        qry = [Setting.GROUP_USER, menuNo]
        str = pyoracle.callfunc('pkg_nrtest.get_tst_case', 'str', qry)

        #字符串转list
        rslt = eval(str)
        if (len(rslt) == 0):
            print('请确认以下配置项是否正确：\n1,配置文件（nari_test.conf）的user_group项：%s \n2,菜单编号：%s' % tuple(qry))
        print('当前用例数据：\n', rslt)

        #dict转Dict ljf
        for i in range(len(rslt)):
            rslt[i] = Dict(rslt[i])
        return rslt
if __name__=='__main__':

    str =DataAccess.getCaseData("99911400")
    print(str)


