# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.GatherQualityAnalyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.curCollectSuccessRate_page import \
    CurCollectSuccessRatePage, CurCollectSuccessRateLocators
from com.nrtest.sea.task.commonMath import *


@ddt
class TestCurCollectSuccessRate(unittest.TestCase, CurCollectSuccessRatePage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GatherQualityAnalyze_data.curCollectSuccessRate_para)

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
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        sleep(2)
        self.exec_script(CurCollectSuccessRateLocators.START_DATE_JS)
        self.exec_script(CurCollectSuccessRateLocators.END_DATE_JS)
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 开始时间
        self.inputStr_startTime(para['START_TIME'])
        # 结束时间
        self.inputStr_endTime(para["END_TIME"])
        self.btn_qry()
        self.sleep_time(2)
        # # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    def countQuery(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        clickTabPage(GatherQualityAnalyze_data.curCollectSuccessRateCount_tab)
        sleep(2)
        self.exec_script(CurCollectSuccessRateLocators.JS_COUNT)

        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 日期时间
        self.inputStr_dateTime_count(para['DATE_TIME'])

        self.btn_count_qry()
        self.sleep_time(2)
        # # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    def detailQuery(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        clickTabPage(GatherQualityAnalyze_data.curCollectSuccessRateDetail_tab)
        sleep(2)
        self.exec_script(CurCollectSuccessRateLocators.JS_DETAIL)

        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 台区编号
        self.inputStr_platformNo(para['PLATFORM_NO'])
        # 台区名称
        self.inputStr_platformNo(para['PLATFORM_NAME'])
        # 日期时间
        self.inputStr_dateTime_detail(para['DATE_TIME'])

        self.btn_detail_qry()
        self.sleep_time(2)
        # # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.curCollectSuccessRate_para,
                                  GatherQualityAnalyze_data.curCollectSuccessRate_tab))
    def test_A_query(self, para):
        self.query(para)

    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.curCollectSuccessRate_para,
                                  GatherQualityAnalyze_data.curCollectSuccessRateCount_tab))
    def test_CountQuery(self, para):
        self.countQuery(para)

    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.curCollectSuccessRate_para,
                                  GatherQualityAnalyze_data.curCollectSuccessRateDetail_tab))
    def test_DetailQuery(self, para):
        self.detailQuery(para)
