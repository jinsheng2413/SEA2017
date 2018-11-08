# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_upgradeEffectStatistics.py
@time: 2018/9/29 14:22
@desc:
"""
import unittest

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.softwareUpgrading_date import SoftwareUpgrading_data
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.upgradeEffectStatistics_page import \
    UpgradeEffectStatisticsPage
from com.nrtest.sea.task.commonMath import *


# 基本应用→终端管理→软件升级→升级效果统计
@ddt.ddt
class TestUpgradeEffectStstistics(unittest.TestCase, UpgradeEffectStatisticsPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            SoftwareUpgrading_data.UpgradeEffectStatistics_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.refreshPage(cls)

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
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 升级目的
        self.inputSel_upgrade_purpose(para['UPGRADE_PURPOSE'])
        # 点击查询按钮
        self.btn_search()

    @ddt.data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEffectStatistics_para))
    def test_der(self, para):
        self.query(para)

    # 终端升级明细
    def query_tab(self, para):
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['TAB_TREE_ORG_NO'])
        # 终端厂家
        self.inputSel_detail_tmnl_factory(para['TAB_TMNL_FACTORY'])
        # 升级目的
        self.inputSel_detail_upgrade_purpose(para['TAB_UPGRADE_PURPOSE'])
        # 点击查询按钮
        self.btn_detail_search()

    @ddt.data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEffectStatistics_para))
    def test_der_tab(self, para):
        self.clickTabPage('终端升级明细')
        self.query_tab(para)
