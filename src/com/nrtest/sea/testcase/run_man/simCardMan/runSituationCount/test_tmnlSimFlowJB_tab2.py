# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_tmnlSimFlowJB_tab2.py
@time: 2018-11-12 10:52
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.simCardMan.runSituationCount.tmnlSimFlowJB_data import RunSituationCount_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.simCardMan.runSituationCount.tmnlSimFlowJB_page import TmnlSimFlowJB_2Page


# 运行管理--SIM卡管理--运行情况分析--终端流量统计（冀北）（第一个tab页）
@ddt
class Test_TnmlSimFlowJB_2(TestCase, TmnlSimFlowJB_2Page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(RunSituationCount_data.para_TmnlSimFlowJB)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(RunSituationCount_data.TmnlSimFlowJB_tab_count_month)
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
        self.inputDt_query_date(para['DATE'])

        # 流量状态
        self.inputChk_flow_status(para['FLOW_STATUS'])

        # # 点击零流量
        # self.click(TmnlSimFlowJB_2Locators.QRY_ZERO_FLOW)

        # 查询
        self.btn_qry()
        self.sleep_time(2)
        # result = self.assert_context(TmnlSimFlowJB_2Locators.TAB_ONE)
        # self.assertTrue(result)

    # @BeautifulReport.add_test_img()
    # @data(*DataAccess.getCaseData(RunSituationCount_data.para_TmnlSimFlowJB,
    #                               RunSituationCount_data.TmnlSimFlowJB_tab_count_month))
    # def test_query(self, para):
    #     self.query(para)

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
    @data(*DataAccess.getCaseData(RunSituationCount_data.para_TmnlSimFlowJB,
                                  RunSituationCount_data.TmnlSimFlowJB_tab_count_month))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RunSituationCount_data.para_TmnlSimFlowJB,
                                  RunSituationCount_data.TmnlSimFlowJB_tab_count_month, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
