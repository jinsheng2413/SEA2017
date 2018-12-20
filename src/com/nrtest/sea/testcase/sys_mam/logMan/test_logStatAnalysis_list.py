# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_logStatAnalysis_fail.py
@time: 2018/11/21 0021 14:08
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.logMan.logMan_data import LogEdit_data
from com.nrtest.sea.pages.sys_mam.logMan.logStatAnalysis_page import *
from com.nrtest.sea.task.commonMath import *


# 系统管理--》日志管理--》日志统计分析
@ddt
class TestLogStatAnalysis_list(unittest.TestCase, LogStatAnalysis_list_Page):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(LogEdit_data.logStatAnalysis_para)
        clickTabPage(LogEdit_data.logStatAnalysis_tab_list)
        sleep(2)
        cls.exec_script(cls, LogStatAnalysis_list_Locators.START_DATE_JS)
        cls.exec_script(cls, LogStatAnalysis_list_Locators.END_DATE_JS)

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
        # 查询时间
        self.inputStr_queryDate(para['QUERY_DATE'])
        # 到
        self.inputStr_TO(para['TO'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LogStatAnalysis_list_Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LogEdit_data.logStatAnalysis_para, LogEdit_data.logStatAnalysis_tab_list))
    def test_query(self, para):
        self.query(para)
