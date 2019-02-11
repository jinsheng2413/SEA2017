# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_meterDataQuery.py
@time: 2018/10/10 9:41
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.meterDataQuery_page import MeterDataQueryPage


# 统计查询→综合查询→抄表数据查询
@ddt
class TestMeterDataQuery(TestCase, MeterDataQueryPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SynthQuery_data.MeterDataQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage()
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
        # 数据类型
        self.inputChk_data_type(para['DATA_TYPE'])
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 抄表段号
        self.inputStr_mr_sect_no(para['MR_SECT_NO'])
        # 电表资产号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 相位
        self.inputSel_phase_code(para['PHASE_CODE'])
        # 查询日期
        self.inputDt_query_date(para['QUERY_DATE'])
        # 数据类别
        self.inputSel_data_type(para['DATA_TYPE'])
        # 电能表抄读状态
        self.inputSel_meter_read_status(para['METER_READ_STATUS'])
        # 终端运行状态
        self.inputSel_tmnl_run_status(para['TMNL_RUN_STATUS'])
        # 农排用户选择
        self.inputSel_user_select(para['USER_SELECT'])
        # 用户类别
        self.inputSel_cons_sort(para['CONS_SORT'])
        # 采集情况
        self.inputChk_read_status(para['READ_STATUS'])
        # 查询按钮
        self.btn_search()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(AssertResult().check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterDataQuery_para))
    def test_query(self, para):
        """统计查询→综合查询→抄表数据查询

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterDataQuery_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
