# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_tmnlSimFlowJB_tab1.py
@time: 2018-11-12 10:27
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.simCardMan.simCardMan_data import SimCardManData
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.simCardMan.runSituationCount.tmnlSimFlowJB_page import TmnlSimFlowJB_1Page


# 运行管理→SIM卡管理→运行情况分析→终端流量统计（冀北）：日流量统计
@ddt
class Test_TnmlSimFlowJB_1(TestCase, TmnlSimFlowJB_1Page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SimCardManData.para_TmnlSimFlowJB)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SimCardManData.TmnlSimFlowJB_tab_count_day)
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
        # 打开左边树选择供电单位
        self.openLeftTree(para['TREE_NODE'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # Sim卡号
        self.inputStr_sim_no(para['SIM_NO'])
        # 开始日期
        self.inputDt_start_date(para['START_DATE'])
        # 结束日期
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
    @data(*DataAccess.getCaseData(SimCardManData.para_TmnlSimFlowJB,
                                  SimCardManData.TmnlSimFlowJB_tab_count_day))
    def test_query(self, para):
        """运行管理→SIM卡管理→运行情况分析→终端流量统计（冀北）：日流量统计
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SimCardManData.para_TmnlSimFlowJB,
                                  SimCardManData.TmnlSimFlowJB_tab_count_day, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
