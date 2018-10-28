# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_upgradeEditionMan.py
@time: 2018/9/25 17:02
@desc:
'''
import unittest

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.softwareUpgrading_date import SoftwareUpgrading_data
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeEditionMan_locators import \
    UpgradeEditionManLocators
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.upgradeEditionMan_page import UpgradeEditionManPage
from com.nrtest.sea.task.commonMath import *


# 基本应用→终端管理→软件升级→升级版本管理
@ddt.ddt
class TestUpgradeEditionMan(unittest.TestCase, UpgradeEditionManPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SoftwareUpgrading_data.UpgradeEditionMan_para)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        # self.clear_values(UpgradeEditionManPage)
        # 回收左边树
        self.recoverLeftTree()

    # 终端版本信息登记
    def query(self, para):
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        # 终端用途
        self.inputSel_tmnl_purpose(para['TMNL_PURPOSE'])
        # #软件版本号
        # self.inputSel_software_version_no(para['SOFTWARE_VERSION_NO'])
        # 点击查询按钮
        self.btn_search()
        # 校验
        result = self.assert_context(*UpgradeEditionManLocators.CHECK)
        self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEditionMan_para))
    def test_a_der(self, para):
        self.query(para)

    # 升级版本管理
    def query_upgrade(self, para):
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
        # 校验
        result = self.assert_context(*UpgradeEditionManLocators.UPGRADE_CHECK)
        self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEditionMan_para))
    def test_b_der(self, para):
        self.clickTabPage('升级版本管理')
        self.query_upgrade(para)

    # 终端版本召测
    def query_edition(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 终端厂家
        self.inputSel_edition_tmnl_factory(para['EDITION_TMNL_FACTORY'])
        # 终端类型
        self.inputSel_edition_tmnl_type(para['EDITION_TMNL_TYPE'])
        # 终端用途
        self.inputSel_edition_tmnl_purpose(para['EDITION_TMNL_PURPOSE'])
        # 终端规约
        self.inputSel_edition_tmnl_protocol(para['EDITION_TMNL_PROTOCOL'])
        # 终端地址
        self.inputStr_edition_tmnl_addr(para['EDITION_TMNL_ADDR'])
        # 查询按钮
        self.btn_edition_search()
        # 校验
        result = self.assert_context(*UpgradeEditionManLocators.EDITION_CHECK)
        self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEditionMan_para))
    def test_c_der(self, para):
        self.clickTabPage('终端版本召测')
        self.query_edition(para)
