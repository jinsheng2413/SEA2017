# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_loadDayData.py
@time: 2019/1/31 0031 16:05
@desc:
"""
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.onlyChangeSysthesisQuery import LoadDayDataPage


# 统计查询→综合查询→专公变综合查询:负荷日数据
@ddt
class test_LoadDayData(TestCase, LoadDayDataPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SynthQuery_data.onlyChangeSysthesisQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.onlyChangeSysthesisQuery_loadDayData_tab)
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
        # 用户编号
        self.openLeftTree(para['TREE_NODE'])
        sleep(1)

        # 数据类型
        self.inputChk_data_type(para['DATA_TYPE'])

        # 终端地址
        self.inputSel_tmnl_addr(para['TMNL_ADDR'])

        # 电能表
        self.inputSel_meter(para['METER'])

        # 时段类型
        self.inputChk_time_type(para['TIME_TYPE'])

        if self.get_para_value(para['TIME_TYPE']) == '日数据':
            # 日期
            self.inputDt_query_date(para['QUERY_DATE'])
        else:
            # 日期从
            self.inputDt_from_date(para['FROM_DATE'])
            # 到
            self.inputDt_to_date(para['TO_DATE'])

        # 功率电流平度
        self.inputChk_pi_balance_type(para['PI_BALANCE_TYPE'])

        # 一二次侧
        self.inputSel_ps_side(para['PS_SIDE'])

        # PQUI
        self.inputChk_pqui(para['PQUI'])

        # 查询
        self.btn_qry()

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
    @data(*DataAccess.getCaseData(SynthQuery_data.onlyChangeSysthesisQuery_para,
                                  SynthQuery_data.onlyChangeSysthesisQuery_loadDayData_tab))
    def test_query(self, para):
        """统计查询→综合查询→专公变综合查询:负荷日数据
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.onlyChangeSysthesisQuery_para,
                                  SynthQuery_data.onlyChangeSysthesisQuery_loadDayData_tab, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
