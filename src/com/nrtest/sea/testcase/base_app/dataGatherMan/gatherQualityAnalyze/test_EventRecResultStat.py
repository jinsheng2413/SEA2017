# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.GatherQualityAnalyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.eventRecResultStat_Page import \
    EventRecResultStatPage, EventRecResultStatLocators
from com.nrtest.sea.task.commonMath import *


# 基本应用→数据采集管理→采集质量分析→事件记录结果统计
@ddt
class TestEventRecResultStat(unittest.TestCase, EventRecResultStatPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GatherQualityAnalyze_data.eventRecResultStat_para)
        sleep(2)
        cls.exec_script(cls, EventRecResultStatLocators.START_DATE_JS)
        cls.exec_script(cls, EventRecResultStatLocators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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
        self.clear_values(EventRecResultStatPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        sleep(2)
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 开始时间
        self.inputStr_start_timme(para['START_TIME'])
        # 结束时间
        self.inputStr_end_time(para['END_TIME'])
        # 时间类型
        self.inputSel_event_type(para['EVENT_TYPE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*EventRecResultStatLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.eventRecResultStat_para))
    def test_query(self, para):
        self.query(para)
