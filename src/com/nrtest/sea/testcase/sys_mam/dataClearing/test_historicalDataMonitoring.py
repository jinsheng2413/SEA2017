# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_historicalDataMonitoring.py
@time: 2018/11/20 0020 11:31
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.dataClearing.dataClearing_data import DataClearing_data
from com.nrtest.sea.pages.sys_mam.dataClearing.historicalDataMonitoring_page import HistoricalDataMonitoringPage, \
    HistoricalDataMonitoringLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理-->数据清理管理-->历史数据监控
@ddt
class TestHistoricalDataMonitoring(unittest.TestCase, HistoricalDataMonitoringPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(DataClearing_data.historicalDataMonitoring_para)
        sleep(2)
        cls.exec_script(cls, HistoricalDataMonitoringLocators.START_DATE_JS)
        cls.exec_script(cls, HistoricalDataMonitoringLocators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 数据组
        self.inputSel_dataGroup(para['DATA_GROUP'])
        # 表名称
        self.inputStr_listName(para['LIST_NAME'])
        # 数据来源
        self.inputSel_data_from(para['DATA_FROM'])
        # 开始日期
        self.inputStr_Start_time(para['START_DATE'])
        # 结束日期
        self.inputStr_end_time(para['END_DATE'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*HistoricalDataMonitoringLocators.BTN_QRY)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataClearing_data.historicalDataMonitoring_para))
    def test_query(self, para):
        self.query(para)
