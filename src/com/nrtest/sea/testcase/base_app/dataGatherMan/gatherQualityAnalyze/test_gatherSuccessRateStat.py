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

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.GatherQualityAnalyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_page import *
from com.nrtest.sea.task.commonMath import *


# 基本应用→数据采集管理→采集质量分析→采集成功率→采集成功率统计
@ddt
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
        self.menu_name = para['MENU_NAME']
        clickTabPage('采集成功率统计')
        sleep(2)
        # 数据类型
        self.inputChk_data_type(para['DATA_TYPE'])
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
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
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate,
                                  GatherQualityAnalyze_data.GatherSuccessRate_tabName_stat))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate,
                                  GatherQualityAnalyze_data.GatherSuccessRate_tabName_stat))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
