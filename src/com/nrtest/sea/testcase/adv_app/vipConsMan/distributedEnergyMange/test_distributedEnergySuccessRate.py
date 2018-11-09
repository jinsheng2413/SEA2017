# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_distributedEnergySuccessRate.py
@time: 2018/11/9 9:25
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyManage_data import \
    DistributedEnergyMange_data
from com.nrtest.sea.pages.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyMonitor_page import \
    DistributedEnergySuccessRatePage
from com.nrtest.sea.task.commonMath import *


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集成功率
@ddt
class TestDistributedEnergySuccessRate(unittest.TestCase, DistributedEnergySuccessRatePage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            DistributedEnergyMange_data.DistributedEnergyMonitor_para, True)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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

    def query(self, para):
        clickTabPage('分布式电源采集成功率')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DistributedEnergyMange_data.DistributedEnergyMonitor_para, tabName='分布式电源采集成功率'))
    def test_der(self, para):
        self.query(para)
