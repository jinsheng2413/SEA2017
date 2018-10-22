# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_orgNoDataQuery.py
@time: 2018/9/29 15:42
@desc:
'''

import unittest
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.locators.stat_rey.synthQuery.orgNoDataQuery_locators import OrgNoDataQueryLocator
from com.nrtest.sea.pages.stat_rey.synthQuery.orgNoDataQuery_page import OrgNoDataPage
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.task.commonMath import *
import ddt

#统计查询→综合查询→供电单位数据查询
@ddt.ddt
class TestUpgradeEffectStstistics(unittest.TestCase,OrgNoDataPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.OrgNoDataQuery_para)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        # 去除查询干扰数据(要传入对应的page页面类)
        self.clear_values(OrgNoDataPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        #打开左边树选择供电单位
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        #日期
        self.inputDt_date(para['DATE'])
        #查询按钮
        self.btn_search()
        #校验
        result = self.assert_context(*OrgNoDataQueryLocator.CHECK_FIRST)
        self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(SynthQuery_data.OrgNoDataQuery_para))
    def test_der(self, para):
        self.query(para)
