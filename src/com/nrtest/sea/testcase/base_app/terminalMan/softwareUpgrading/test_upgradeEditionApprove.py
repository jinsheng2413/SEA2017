# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_upgradeEditionApprove.py
@time: 2018/9/27 16:17
@desc:
'''

from com.nrtest.common.dictionary import Dict
import unittest
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeEditionApprove_locators import UpgradeEditionApproveLocators
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.upgradeEditionApprove_page import UpgradeEditionApprovePage
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.upgradeEditionApprove_data import UpgradeEditionApprove_date
from com.nrtest.sea.task.commonMath import *
import ddt
from com.nrtest.common.base_page import *

# 基本应用→终端管理→软件升级→升级版本审计
@ddt.ddt
class TestUpgradeEditionApprove(unittest.TestCase,UpgradeEditionApprovePage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(UpgradeEditionApprove_date.para_UpgradeEditionApprove)

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


    def query(self, para):
        #终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        #终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        #终端用途
        self.inputSel_tmnl_purpose(para['TMNL_PURPOSE'])
        #申请状态
        self.inputSel_apply_status(para['APPLY_STATUS'])
        #申请开始日期
        self.start_date(para['START_DATE'])
        #申请结束日期
        self.end_date(para['END_DATE'])
        # 点击查询按钮
        self.btn_search()

    @ddt.data(*DataAccess.getCaseData(UpgradeEditionApprove_date.para_UpgradeEditionApprove))
    def test_der(self, para):
        self.query(para)
