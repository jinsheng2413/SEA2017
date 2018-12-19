# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_gatherSuccessRateStat.py
@time: 2018/12/4 16:28
@desc:
"""

import unittest
from time import sleep

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.GatherQualityAnalyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_page import *
from com.nrtest.sea.task.commonMath import *


# 基本应用→数据采集管理→采集质量分析→采集成功率→采集成功率统计
@ddt.ddt
class TestGatherSuccessRateStat(unittest.TestCase, GatherSuccessRateStatPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GatherQualityAnalyze_data.para_GatherSuccessRate)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新菜单页面
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
        sleep(2)
        clickTabPage('采集成功率统计')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 用户类型
        self.inputCSel_cons_type(para['CONS_TYPE'])
        # 通信方式
        self.inputSel_comm_type(para['COMM_TYPE'])
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 芯片厂家
        self.inputSel_chip_factory(para['CHIP_FACTORY'])
        # 通讯规约
        self.inputSel_tmnl_protocol(para['TMNL_PROTOCOL'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 点击查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        # result = self.assert_context(*GatherSuccessRateStatLocators.CHECK_FIRST)
        # self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate,
                                      GatherQualityAnalyze_data.GatherSuccessRate_tabName_stat))
    def test_a_der(self, para):
        self.query(para)
