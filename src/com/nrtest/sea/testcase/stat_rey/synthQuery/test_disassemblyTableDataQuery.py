# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_disassemblyTableDataQuery.py
@time: 2018/10/9 14:21
@desc:
"""
from asyncio import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.disassemblyTableDataQuery_page import DisassemblyTableDataQueryPage


# 统计查询→综合查询→销户和拆表数据查询
@ddt
class TestDisassemblyTableDataQuery(TestCase, DisassemblyTableDataQueryPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SynthQuery_data.DisassemblyTableDataQuery_para)
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
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 电能表资产号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 开始时间
        self.inputDt_start_date(para['START_DATE'])
        # 结束时间
        self.inputDt_end_date(para['END_DATE'])
        # 查询按钮
        self.btn_search()
        tab_name = self.get_para_value(para['TAB_NAME'])
        if bool(tab_name):
            #  选择指定行
            self.inputRow_select_row(para['SELECT_ROW'])
            # TAB页名称
            self.inputChk_tab_name(para['TAB_NAME'])
            sleep(0.5)
            # TAB页开始日期
            self.inputDt_tab_start_date(para['TAB_START_DATE'])
            # TAB页结束日期
            self.inputDt_tab_end_date(para['TAB_END_DATE'])
            if tab_name == '负荷曲线类数据':
                # 曲线类型
                self.inputSel_curve_type(para['CURVE_TYPE'])
            self.btn_qry()

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
    @data(*DataAccess.getCaseData(SynthQuery_data.DisassemblyTableDataQuery_para))
    def test_query(self, para):
        """统计查询→综合查询→销户和拆表数据查询
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.DisassemblyTableDataQuery_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
