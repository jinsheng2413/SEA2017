# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_upgradeResultConfirmation.py
@time: 2018/9/29 10:07
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.softwareUpgrading_data import SoftwareUpgrading_data
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.upgradeResultConfirmation_page import \
    UpgradeResultConfirmationPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→终端管理→软件升级→升级结果确认
@ddt
class TestUpgradeResultConfirmation(TestCase, UpgradeResultConfirmationPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SoftwareUpgrading_data.UpgradeResultConfirmation_para)
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
        # 升级号
        self.inputChk_upgrade_no(para['UPGRADE_NO'])
        # 打开左边树选择供电单位
        self.openLeftTree(para['TREE_NODE'])
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        # 终端用途
        self.inputSel_tmnl_purpose(para['TMNL_PURPOSE'])
        # 升级版本号
        self.inputSel_upgrade_version_no(para['UPGRADE_VERSION_NO'])
        # 升级目的
        self.inputSel_upgrade_purpose(para['UPGRADE_PURPOSE'])
        # 确认状态
        self.inputSel_affirm_status(para['AFFIRM_STATUS'])
        # 升级状态
        self.inputSel_upgrade_status(para['UPGRADE_STATUS'])
        # 批次号
        self.inputStr_batch_no(para['BATCH_NO'])
        # 前置下发状态
        self.inputSel_preposition_down_status(para['PREPOSITION_DOWN_STATUS'])
        # 确认开始日期
        self.inputDt_start_date(para['START_DATE'])
        # 确认结束日期
        self.inputDt_end_date(para['END_DATE'])
        # 点击查询按钮
        self.btn_query()

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
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeResultConfirmation_para))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeResultConfirmation_para))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
