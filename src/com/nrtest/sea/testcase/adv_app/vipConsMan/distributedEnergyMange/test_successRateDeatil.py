# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_successRateDeatil.py
@time: 2018/11/9 14:27
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyManage_data import \
    DistributedEnergyMange_data
from com.nrtest.sea.pages.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyQuality_page import \
    SuccessRateDetailPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率明细
@ddt
class TestSuccessRateDetail(unittest.TestCase, SuccessRateDetailPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            DistributedEnergyMange_data.DistributedEnergyQuality_para, True)

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
        clickTabPage('采集成功率明细')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 电能表用途
        self.inputSel_meter_purpose(para['METER_PURPOSE'])
        # 发电类型
        self.inputSel_elec_type(para['ELEC_TYPE'])
        # 发电量消纳方式
        self.inputSel_abso_type(para['ABSO_TYPE'])
        # 日期
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DistributedEnergyMange_data.DistributedEnergyQuality_para, tabName='采集成功率明细'))
    def test_der(self, para):
        self.query(para)
