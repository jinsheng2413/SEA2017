# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_meterRealTimePowerCutQuery.py
@time: 2018/11/6 15:27
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutAnalysis_data import \
    PowerCutAnalysis_data
from com.nrtest.sea.pages.adv_app.variationMonitorAnalysis.powerCutAnalysis.meterRealTimePowerCutQuery_page import \
    MeterRealTimePowerCutQueryPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→配变监测分析→停电分析→表计实时停上电信息查询
@ddt
class TestMeterRealTimePowerCutQuery(TestCase, MeterRealTimePowerCutQueryPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(PowerCutAnalysis_data.MeterRealTimePowerCutQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage()
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        self.openLeftTree(para['TREE_NODE'])
        # 台区编号
        self.inputStr_tg_no(para['TG_NO'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 电表资产号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 停电标志
        self.inputSel_power_cut_flag(para['POWER_CUT_FLAG'])
        # 查询类型
        self.inputChk_qry_date_type(para['QRY_DATE_TYPE'])
        val = self.get_para_value(para['QRY_DATE_TYPE'])
        if val == '按时间段查询':
            # 开始日期
            self.inputDt_start_date(para['START_DATE'])
            # 结束日期
            self.inputDt_end_date(para['END_DATE'])
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

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.MeterRealTimePowerCutQuery_para))
    def test_query(self, para):
        """高级应用→配变监测分析→停电分析→表计实时停上电信息查询

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.MeterRealTimePowerCutQuery_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
