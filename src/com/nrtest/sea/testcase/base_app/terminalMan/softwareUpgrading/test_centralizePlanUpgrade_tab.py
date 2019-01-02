# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_centralizePlanUpgrade_tab.py
@time: 2018/12/26 10:11
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.softwareUpgrading_data import SoftwareUpgrading_data
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.centralizePlanUpgrade_page import \
    CentralizePlanUpgradePage
from com.nrtest.sea.task.commonMath import *


# 基本应用→终端管理→软件升级→集中计划升级→制定计划
@ddt
class TestUpgradeTaskExecution(TestCase, CentralizePlanUpgradePage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SoftwareUpgrading_data.CentralizedPlanUpgrade_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SoftwareUpgrading_data.CentralizedPlanUpgrade_tabName_plan)
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

    # 制定计划
    def query(self, para):
        clickTabPage('制定计划')
        # 打开左边树选择供电单位
        openLeftTree(para['TREE_NODE'])
        # 忽略旧版本号
        self.inputChk_history_version(para['HISTORY_VERSION'])
        # 终端厂家
        self.inputSel_tab_tmnl_factory(para['TAB_TMNL_FACTORY'])
        # 终端类型
        self.inputSel_tab_tmnl_type(para['TAB_TMNL_TYPE'])
        # 终端用途
        self.inputSel_tab_tmnl_purpose(para['TAB_TMNL_PURPOSE'])
        # 升级版本号
        self.inputSel_tab_upgrade_version_no(para['TAB_UPGRADE_VERSION_NO'])
        # 点击查询按钮
        self.btn_tab_search()

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
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.CentralizedPlanUpgrade_para,
                                  SoftwareUpgrading_data.CentralizedPlanUpgrade_tabName_plan))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.CentralizedPlanUpgrade_para,
                                  SoftwareUpgrading_data.CentralizedPlanUpgrade_tabName_plan))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)