# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_meterSuccessRateQuery_failed.py
@time: 2018/10/10 15:07
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.meterSuccessRateQuery_page import MeterSuccessRateQueryFailedPage


# 统计查询→综合查询→抄表成功率查询（河北）:连续抄表失败明细
@ddt
class TestMeterSuccessRateFailedQuery(TestCase, MeterSuccessRateQueryFailedPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SynthQuery_data.MeterSuccessRateQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.MeterSuccessRateQuery_tabName_failed)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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
        # Tab页选项选择
        self.inputChk_tab_name(para['TAB_NAME'])

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 运行状态
        self.inputSel_run_status(para['RUN_STATUS'])

        if self.get_para_value(para['TAB_NAME']) == '连续抄表失败统计':
            # 日期
            self.inputDt_query_date(para['QUERY_DATE'])
        else:
            # 接线方式
            self.inputSel_wiring_mode(para['WIRING_MODE'])
            # 用户编号
            self.inputStr_cons_no(para['CONS_NO'])
            # 终端地址
            self.inputStr_tmnl_addr(para['TMNL_ADDR'])
            # 农排用户选择
            self.inputSel_user_select(para['USER_SELECT'])
            # 连续失败天数
            self.inputStr_read_fail_days_start(para['READ_FAIL_DAYS_START'])
            # 到
            self.inputStr_read_fail_days_end(para['READ_FAIL_DAYS_END'])

        # 查询按钮
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
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterSuccessRateQuery_para,
                                  SynthQuery_data.MeterSuccessRateQuery_tabName_failed))
    def test_query(self, para):
        """统计查询→综合查询→抄表成功率查询（河北）:连续抄表失败明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterSuccessRateQuery_para,
                                  SynthQuery_data.MeterSuccessRateQuery_tabName_failed, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
