# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_tgLineLossAnalysis.py
@time: 2018/10/30 14:09
@desc:
"""

import unittest
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossStatisticsAnalysis_data import \
    LineLossStatisticsAnalysis_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.tgLineLossAnalysis_page import \
    TgLineLossAnalysisPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→线损统计分析→台区线损分析
@ddt
class TestTgLineLossAnalysis(unittest.TestCase, TgLineLossAnalysisPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LineLossStatisticsAnalysis_data.TgLineLossAnalysis_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        menuPage.remove_dt_readonly()


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
        sleep(2)
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 台区编号
        self.inputStr_tg_no(para['TG_NO'])
        # 台区名称
        self.inputStr_tg_name(para['TG_NAME'])
        # 安装率
        self.inputSel_installation_rate(para['INSTALLATION_RATE'])
        # self.inputStr_installation_rate(para['INSTALLATION_RATE_INPUT'])
        # 抄读成功率
        self.inputSel_read_success_rate(para['READ_SUCCESS_RATE'])
        # self.inputStr_read_success_rate(para['READ_SUCCESS_RATE_INPUT'])
        # 线损率
        self.inputSel_line_loss_rate(para['LINE_LOSS_RATE'])
        # self.inputStr_line_loss_rate(para['LINE_LOSS_RATE_INPUT'])
        # 输入日期
        self.inputDT_date(para['QUERY_DATE'])
        # 按日期类型
        self.inputDTT_type_sel(para['DATE_TYPE_SEL'])
        # 点击复选框
        self.inputChkRunType(para['LINE_LOSS_TYPE'])
        if self.get_para_value(para['LINE_LOSS_TYPE']) == '可算':
            # 点击达标
            self.inputChk_T(para['TG_TYPE'])
        # 查询按钮
        self.btn_search()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(self.check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    # @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.TgLineLossAnalysis_para)[0:1])
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.TgLineLossAnalysis_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
