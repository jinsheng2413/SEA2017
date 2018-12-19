# -*- coding: utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_sectFailedAppQuery.py
@time: 2018/10/29 11:24
@desc:
'''

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.appDispose.appDispose_data import AppDispose_data
from com.nrtest.sea.pages.adv_app.appDispose.sectfailedAppQuery_page import SectfailedAppQueryPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→工单处理→抄表失败工单查询
@ddt
class TestAssetMan(unittest.TestCase, SectfailedAppQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(AppDispose_data.SectFailedAppQuery_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.refreshPage(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 抄表段号
        self.inputStr_sect_no(para['SECT_NO'])
        # 抄表管理员工号
        self.inputStr_sect_manager_no(para['SECT_MANAGER_NO'])
        # 查询按钮
        self.btn_search()

    @data(*DataAccess.getCaseData(AppDispose_data.SectFailedAppQuery_para))
    def test_der(self, para):
        self.query(para)
