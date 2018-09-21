# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: TestGatherSuccessRate.py
@time: 2018-09-17 16:30
@desc:
'''

from com.nrtest.common.dictionary import Dict
import unittest
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_locators import \
    GatherSuccessRateLocators
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_page import \
    GatherSuccessRatePage
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_data import \
    GatherSuccessRate_data
from com.nrtest.sea.task.commonMath import *
import ddt
from com.nrtest.common.base_page import *


# 基本应用→数据采集管理→采集质量分析→采集成功率
from com.nrtest.sea.testcase.adv_app.costControlManage.kl import ly


@ddt.ddt

class TestGatherSuccessRate(unittest.TestCase, GatherSuccessRatePage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GatherSuccessRate_data.para_GatherSuccessRate)
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

    @ddt.data(*DataAccess.getCaseData(GatherSuccessRate_data.para_GatherSuccessRate))
    def test_der(self, para):
        self.query(Dict(para))

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
        # 校验
        result = self.assert_context(*GatherSuccessRateLocators.STATISTICS_CHECK)
        self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(GatherSuccessRate_data.para_GatherSuccessRate))
    def test_der_statistics(self,para):
        self.clickTabPage('采集成功率统计')
        self.query_statistics(Dict(para))
