# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_gatherSuccessRate.py
@time: 2018-09-17 16:30
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.gather_quality_analyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_page import \
    GatherSuccessRatePage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→数据采集管理→采集质量分析→采集成功率:采集成功率
@ddt
class TestGatherSuccessRate(TestCase, GatherSuccessRatePage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(GatherQualityAnalyze_data.GatherSuccessRate_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(GatherQualityAnalyze_data.GatherSuccessRate_tabName)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新菜单页面
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
        self.openLeftTree(para['TREE_NODE'])
        # 数据类型
        self.inputChk_data_type(para['DATA_TYPE'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 计量方式
        self.inputSel_meas_mode(para['MEAS_MODE'])
        # 所属区域
        self.inputSel_area(para['AREA'])
        # 芯片厂家
        self.inputSel_chip_factory(para['CHIP_FACTORY'])
        # 开始时间
        self.inputDt_start_date(para['START_DATE'])
        # 结束时间
        self.inputDt_end_date(para['END_DATE'])
        # 相位
        self.inputSel_phase_code(para['PHASE_CODE'])
        # 点击查询按钮
        self.btn_search()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.GatherSuccessRate_para,
                                  GatherQualityAnalyze_data.GatherSuccessRate_tabName))
    def test_query(self, para):
        """基本应用→数据采集管理→采集质量分析→采集成功率:采集成功率

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.GatherSuccessRate_para,
                                  GatherQualityAnalyze_data.GatherSuccessRate_tabName))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
