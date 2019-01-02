# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_indexAllocation.py
@time: 2018/11/2 14:19
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.personalizedIndexDisplay.personalizedIndexDisplay_data import \
    PersonalizedIndexDisplay_data
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.personalizedIndexDisplay.indexAllocation_locators import \
    IndexAllocationLocators
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.personalizedIndexDisplay.indexAllocation_page import \
    IndexAllocationPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→同期线损→指标配置
@ddt
class TestIndexAllocation(unittest.TestCase, IndexAllocationPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(PersonalizedIndexDisplay_data.IndexAllocation_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭菜单页面
        cls.closePages(cls)

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
        openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 台区编号
        self.inputStr_tg_no(para['TG_NO'])
        # 台区状态
        self.inputSel_tg_status(para['TG_STATUS'])
        # 责任人工号
        self.inputStr_charge_person_no(para['CHARGE_PERSON_NO'])
        # 查询按钮
        self.btn_search()
        # 校验
        result = self.assert_context(IndexAllocationLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PersonalizedIndexDisplay_data.IndexAllocation_para))
    def test_der(self, para):
        self.query(para)
