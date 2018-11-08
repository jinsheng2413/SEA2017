# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_indexDetail.py
@time: 2018/11/2 15:02
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.personalizedIndexDisplay.personalizedIndexDisplay_data import \
    PersonalizedIndexDisplay_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.personalizedIndexDisplay.indexDetail_page import IndexDetailPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→同期线损→指标明细
@ddt
class TestIndexDetail(unittest.TestCase, IndexDetailPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            PersonalizedIndexDisplay_data.IndexDetail_para, True)

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
        clickTabPage('指标明细')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 台区编号
        self.inputStr_tg_no(para['TG_NO'])
        # 台区名称
        self.inputStr_tg_name(para['TG_NAME'])
        # 时间选择
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PersonalizedIndexDisplay_data.IndexDetail_para))
    def test_der(self, para):
        self.query(para)
