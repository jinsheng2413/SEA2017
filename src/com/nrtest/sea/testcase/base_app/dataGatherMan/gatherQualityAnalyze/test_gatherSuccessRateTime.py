# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_gatherSuccessRateTime.py
@time: 2018/12/6 11:35
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


# 基本应用→数据采集管理→采集质量分析→采集成功率→按时间统计
@ddt.ddt
class TestGatherSuccessRateTime(unittest.TestCase, GatherSuccessRateTimePage):
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
        clickTabPage('按时间统计')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 查询日期，开始
        self.inputDt_start_date(para['START_DATE'])
        # 查询日期，结束
        self.inputDt_end_date(para['END_DATE'])
        # 用户类型
        self.inputCSel_cons_type(para['CONS_TYPE'])
        # 用户范围
        self.inputSel_user_range(para['USER_RANGE'])
        # 停电标志
        self.inputSel_power_cut_sign(para['POWER_CUT_SIGN'])
        # 终端类型
        self.inputCSel_tmnl_type(para['TMNL_TYPE'])
        # 通信方式
        self.inputCSel_comm_way(para['COMM_WAY'])
        # 规约类型
        self.inputCSel_protocol_type(para['PROTOCOL_TYPE'])
        # 计量方式
        self.inputSel_measure_way(para['MEASURE_WAY'])
        # 点击查询按钮
        # self.btn_search()

    @ddt.data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate,
                                      GatherQualityAnalyze_data.GatherSuccessRate_tabName_time))
    def test_a_der(self, para):
        self.query(para)
