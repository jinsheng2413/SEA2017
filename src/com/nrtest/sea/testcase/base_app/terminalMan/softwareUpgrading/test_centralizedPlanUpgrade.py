# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_centralizedPlanUpgrade.py
@time: 2018/9/29 10:54
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.softwareUpgrading_data import SoftwareUpgrading_data
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.centralizePlanUpgrade_page import \
    CentralizePlanUpgradePage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→终端管理→软件升级→集中计划升级:集中计划升级
@ddt
class TestCentralizedPlanUpgrade(TestCase, CentralizePlanUpgradePage):
    @classmethod
    def setUpClass(cls):

        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SoftwareUpgrading_data.CentralizedPlanUpgrade_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SoftwareUpgrading_data.CentralizedPlanUpgrade_tabName)
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
        # # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(UpgradeTaskExecutionPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树选择供电单位
        self.openLeftTree(para['TREE_NODE'])
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 升级目的
        self.inputSel_upgrade_purpose(para['UPGRADE_PURPOSE'])
        # 终端用途
        self.inputSel_tmnl_purpose(para['TMNL_PURPOSE'])
        # 开始时间
        self.inputDt_start_date(para['START_DATE'])
        # 结束时间
        self.inputDt_end_date(para['END_DATE'])
        # 批次号
        self.inputStr_batch_no(para['BATCH_NO'])
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
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.CentralizedPlanUpgrade_para,
                                  SoftwareUpgrading_data.CentralizedPlanUpgrade_tabName))
    def test_query(self, para):
        """基本应用→终端管理→软件升级→集中计划升级:集中计划升级
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.CentralizedPlanUpgrade_para,
                                  SoftwareUpgrading_data.CentralizedPlanUpgrade_tabName))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
