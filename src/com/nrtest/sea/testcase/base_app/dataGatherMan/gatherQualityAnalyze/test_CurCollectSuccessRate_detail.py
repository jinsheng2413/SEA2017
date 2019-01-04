# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_CurCollectSuccessRate_detail.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.GatherQualityAnalyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.curCollectSuccessRate_page import \
    CurCollectSuccessRatePage, CurCollectSuccessRateLocators
from com.nrtest.sea.task.commonMath import *


# 基本应用→数据采集管理→采集质量分析→实时采集成功率
@ddt
class TestCurCollectSuccessRate(unittest.TestCase, CurCollectSuccessRatePage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GatherQualityAnalyze_data.curCollectSuccessRate_para)
        sleep(2)
        clickTabPage(GatherQualityAnalyze_data.curCollectSuccessRateDetail_tab)

        cls.exec_script(CurCollectSuccessRateLocators.JS_DETAIL)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        # 注册菜单
        self.menu_name = para['MENU_NAME']

        print(para['PLATFORM_NO'])

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 台区编号
        self.inputStr_platformNo(para['PLATFORM_NO'])
        # 台区名称
        self.inputStr_platformNo(para['PLATFORM_NAME'])
        # 日期时间
        self.inputStr_dateTime_detail(para['DATE_TIME'])
        self.btn_query(True)

        # self.btn_query()
        # self.sleep_time(2)

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
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.curCollectSuccessRate_para,
                                  GatherQualityAnalyze_data.curCollectSuccessRateDetail_tab))
    def test_DetailQuery(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.curCollectSuccessRate_para,
                                  GatherQualityAnalyze_data.curCollectSuccessRateDetail_tab))
    def _test_DetailQuery(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
