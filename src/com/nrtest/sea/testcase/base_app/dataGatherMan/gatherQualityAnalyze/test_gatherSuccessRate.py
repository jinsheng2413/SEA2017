# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: TestGatherSuccessRate.py
@time: 2018-09-17 16:30
@desc:
'''

import unittest

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.GatherQualityAnalyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_locators import \
    GatherSuccessRateLocators
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_page import \
    GatherSuccessRatePage
from com.nrtest.sea.task.commonMath import *


# 基本应用→数据采集管理→采集质量分析→采集成功率


@ddt.ddt
class TestGatherSuccessRate(unittest.TestCase, GatherSuccessRatePage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GatherQualityAnalyze_data.para_GatherSuccessRate)
        # cls.exec_script(cls,GatherSuccessRateLocators.CONS_TYPE_JS)
        # cls.exec_script(cls,GatherSuccessRateLocators.STATISTICS_CONS_TYPE_JS)

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
        # 去除查询干扰数据(要传入对应的page页面类)
        self.clear_values(GatherSuccessRatePage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''

        # 基本应用→数据采集管理→采集质量分析→采集成功率→采集成功率
        # 打开左边树并选择
        self.sleep_time(2)
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 用户类型
        self.inputCSel_cons_type(para['CONS_TYPE'])
        # 开始时间
        self.inputDt_start_date(para['START_DATE'])
        # 结束时间
        self.inputDt_end_date(para['END_DATE'])
        # 点击查询按钮
        self.btn_search()
        # 校验
        result = self.assert_context(*GatherSuccessRateLocators.BTN_FIRST_UNIT)
        self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate))
    def test_a_der(self, para):
        self.query(para)

    # 基本应用→数据采集管理→采集质量分析→采集成功率→采集成功率统计
    def query_statistics(self, para):
        # 打开左边树并选择
        self.sleep_time(2)
        self.driver = openLeftTree(para['STATISTICS_TREE_ORG_NO'])
        # 用户类型
        self.inputCSel_statistics_cons_type(para['STATISTICS_CONS_TYPE'])
        # 查询时间
        self.inputDt_statistics_date(para['STATISTICS_DATE'])
        # 点击查询按钮
        self.btn_statistics_search()
        # # 校验
        # result = self.assert_context(*GatherSuccessRateLocators.BTN_FIRST_UNIT)
        # self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate))
    def test_b_der_statistics(self, para):
        self.clickTabPage('采集成功率统计')
        self.query_statistics(para)

    # 基本应用→数据采集管理→采集质量分析→采集成功率→采集成功率明细
    def query_detail(self, para):
        # 打开左边树并选择
        self.sleep_time(2)
        self.driver = openLeftTree(para['DETAIL_TREE_ORG_NO'])
        # 用户类型
        self.inputCSel_detail_cons_type(para['DETAIL_CONS_TYPE'])
        # 查询时间
        self.inputDt_detail_date(para['DETAIL_DATE'])
        # 点击查询按钮
        self.btn_detail_search()
        # # 校验
        # result = self.assert_context(*GatherSuccessRateLocators.BTN_FIRST_UNIT)
        # self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate))
    def test_c_der_detail(self, para):
        self.clickTabPage('采集成功率明细')
        self.query_detail(para)

    # 基本应用→数据采集管理→采集质量分析→采集成功率→连续抄表失败明细
    def query_false(self, para):
        # 打开左边树并选择
        self.sleep_time(2)
        self.driver = openLeftTree(para['FALSE_TREE_ORG_NO'])
        # 用户类型
        self.inputCSel_false_cons_type(para['FALSE_CONS_TYPE'])
        # 查询时间
        self.inputDt_false_date(para['FALSE_DATE'])
        # 点击查询按钮
        self.btn_false_search()
        # # 校验
        # result = self.assert_context(*GatherSuccessRateLocators.BTN_FIRST_UNIT)
        # self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate))
    def test_d_der_false(self, para):
        self.clickTabPage('连续抄表失败明细')
        self.query_false(para)

    #
    # # 基本应用→数据采集管理→采集质量分析→采集成功率→连续抄表失败明细→连续N天抄表失败明细
    #     @ddt.data(*DataAccess.getCaseData(GatherSuccessRate_data.para_GatherSuccessRate))
    #     def test_e_der_false(self,para):
    #         self.clickTabPage('连续抄表失败明细')
    #         self.clickTabPage('连续N天抄表失败明细')
    #         self.query_false(para)
    #
    # # 基本应用→数据采集管理→采集质量分析→采集成功率→连续抄表失败明细→应采集电表明细
    #     @ddt.data(*DataAccess.getCaseData(GatherSuccessRate_data.para_GatherSuccessRate))
    #     def test_f_der_false(self, para):
    #         self.clickTabPage('连续抄表失败明细')
    #         self.clickTabPage('应采集电表明细')
    #         self.query_false(para)

    # 基本应用→数据采集管理→采集质量分析→采集成功率→按时间统计
    def query_date(self, para):
        # 打开左边树并选择
        self.sleep_time(2)
        self.driver = openLeftTree(para['DATE_TREE_ORG_NO'])
        # 用户类型
        self.inputCSel_date_cons_type(para['DATE_CONS_TYPE'])
        # 查询时间,开始
        self.inputDt_data_start_date(para['DATE_START_DATE'])
        # 查询时间，结束
        self.inputDt_data_end_date(para['DATE_END_DATE'])
        # 点击查询按钮
        self.btn_date_search()
        # # 校验
        # result = self.assert_context(*GatherSuccessRateLocators.BTN_FIRST_UNIT)
        # self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(GatherQualityAnalyze_data.para_GatherSuccessRate))
    def test_g_der_date(self, para):
        self.clickTabPage('按时间统计')
        self.query_date(para)
