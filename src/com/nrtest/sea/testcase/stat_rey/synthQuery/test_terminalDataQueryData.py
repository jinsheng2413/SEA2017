# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_terminalDataQueryData.py
@time: 2019-02-15 16:15
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.terminalDataQuery_page import TerminalDataQueryDataPage


# 统计查询→综合查询→终端数据查询:数据展示
@ddt
class TestTerminaldataquery(TestCase, TerminalDataQueryDataPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SynthQuery_data.TmnlDataQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.TmnlDataQuery_DataDisp)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

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
        每个测试用例测试结束后的操作，在这里做相关清理工作
        :return:
        """

        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        if self.is_tree_node_first():
            self.openLeftTree(para['TREE_NODE'])
        else:
            # 终端资产号
            self.inputStr_tmnl_asset_no(para['TMNL_ASSET_NO'])

        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])

        # 父级查询
        self.btn_search()

        # Tab页名称
        self.inputChk_tab_name(para['TAB_NAME'])

        # 总加组
        self.inputSel_added_group(para['ADDED_GROUP'])

        # 查询日期
        self.inputDt_start_date(para['START_DATE'])

        if self.get_para_value(para['TAB_NAME']) == '电量':
            # 至
            self.inputDt_end_date(para['END_DATE'])

        # 查询
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
    @data(*DataAccess.getCaseData(SynthQuery_data.TmnlDataQuery_para, SynthQuery_data.TmnlDataQuery_DataDisp))
    def test_query(self, para):
        """统计查询→综合查询→终端数据查询:数据展示
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.TmnlDataQuery_para, SynthQuery_data.TmnlDataQuery_DataDisp, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
