# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_continuousFalseDetail.py
@time: 2018/12/6 10:52
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


# 基本应用→数据采集管理→采集质量分析→采集成功率→连续抄表失败明细
@ddt.ddt
class TestContinuousFalseDetail(unittest.TestCase, ContinuousFalseDetailPage):
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
        clickTabPage('连续抄表失败明细')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 用户类型
        self.inputCSel_cons_type(para['CONS_TYPE'])
        # 运行状态
        self.inputSel_run_status(para['RUN_STATUS'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 点击查询按钮
        self.btn_search()

    @ddt.data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate,
                                      GatherQualityAnalyze_data.GatherSuccessRate_tabName_continuous))
    def test_a_der(self, para):
        self.query(para)
