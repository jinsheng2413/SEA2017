# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_upgradeEditionMan_upgrade.py
@time: 2018/12/11 9:30
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.softwareUpgrading_data import SoftwareUpgrading_data
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.upgradeEditionMan_page import UpgradeEditionManPage
from com.nrtest.sea.task.commonMath import *


# 基本应用→终端管理→软件升级→升级版本管理→升级版本管理
@ddt
class TestUpgradeEditionMan(unittest.TestCase, UpgradeEditionManPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SoftwareUpgrading_data.UpgradeEditionMan_para)

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
        # self.clear_values(UpgradeEditionManPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 注册菜单
        self.menu_name = para['MENU_NAME']
        clickTabPage('升级版本管理')
        # 终端厂家
        self.inputSel_upgrade_tmnl_factory(para['UPGRADE_TMNL_FACTORY'])
        # 终端类型
        self.inputSel_upgrade_tmnl_type(para['UPGRADE_TMNL_TYPE'])
        # 终端用途
        self.inputSel_upgrade_tmnl_purpose(para['UPGRADE_TMNL_PURPOSE'])
        # 申请状态
        self.inputSel_upgrade_apply_status(para['UPGRADE_APPLY_STATUS'])
        # 申请开始日期
        self.upgrade_start_date(para['UPGRADE_START_DATE'])
        # 申请结束日期
        self.upgrade_end_date(para['UPGRADE_END_DATE'])
        # 点击查询按钮
        self.btn_upgrade_search()

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
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEditionMan_para,
                                  SoftwareUpgrading_data.UpgradeEditionMan_tabName_upgrade))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEditionMan_para,
                                  SoftwareUpgrading_data.UpgradeEditionMan_tabName_upgrade, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
