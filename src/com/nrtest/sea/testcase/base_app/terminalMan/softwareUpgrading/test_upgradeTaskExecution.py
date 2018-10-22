# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_upgradeTaskExecution.py
@time: 2018/9/28 14:29
@desc:
'''

import unittest
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeTaskExecution_locators import UpgradeTaskExecutionLocators
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.upgradeTaskExecution_page import UpgradeTaskExecutionPage
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.softwareUpgrading_date import SoftwareUpgrading_data
from com.nrtest.sea.task.commonMath import *
import ddt

# 基本应用→终端管理→软件升级→升级任务执行
@ddt.ddt
class TestUpgradeTaskExecution(unittest.TestCase,UpgradeTaskExecutionPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SoftwareUpgrading_data.UpgradeTaskExecution_para)

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
        # self.clear_values(UpgradeTaskExecutionPage)
        # 回收左边树
        self.recoverLeftTree()


    def query(self, para):
        #打开左边树选择供电单位
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        #终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        #终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        #终端用途
        self.inputSel_tmnl_purpose(para['TMNL_PURPOSE'])
        #开始时间
        self.inputDt_start_date(para['START_DATE'])
        #结束时间
        self.inputDt_end_date(para['END_DATE'])
        #批次号
        self.inputStr_batch_no(para['BATCH_NO'])
        #升级目的
        self.inputSel_upgrade_purpose(para['UPGRADE_PURPOSE'])
        #升级类型
        self.inputSel_upgrade_type(para['UPGRADE_TYPE'])
        #执行状态
        self.inputSel_execution_state(para['EXECUTION_STATE'])
        # 点击查询按钮
        self.btn_search()

    @ddt.data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeTaskExecution_para))
    def test_der(self, para):
        self.query(para)