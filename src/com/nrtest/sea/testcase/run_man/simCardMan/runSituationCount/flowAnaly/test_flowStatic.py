# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_flowCount.py
@time: 2018/11/9 0009 9:44
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.simCardMan.runSituationCount.runSituationCount_data import RunSituationCount_data
from com.nrtest.sea.locators.run_man.simCardMan.runSituationCount.flowAnaly_locators import FlowCountLocators
# from com.nrtest.sea.pages.run_man.simCardMan.runSituationCount.flowAnaly_page import FlowCountPage
from com.nrtest.sea.task.commonMath import *


# 运行管理-->SIM卡管理-->运行情况分析-->流量分析
@ddt
class TestFlowAnaly(unittest.TestCase,FlowCountPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单
        cls.driver = openMenu(RunSituationCount_data.para_flowAnaly)
        # 点击Tab页标签
        clickTabPage(RunSituationCount_data.para_flowAnaly_detail)
        cls.exec_script(cls,FlowCountLocators.START_DATE_JS)

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

        # 注册菜单
        self.menu_name = para['MENU_NAME']

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        #月份
        self.inputStr_month(para['MONTH_COUNT'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*FlowCountLocators.TAB_ONE)
        # self.assertTrue(result)

    def assert_query_result(self, para):
        """
        查询结果校验
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
    @data(*DataAccess.getCaseData(RunSituationCount_data.para_flowAnaly,
                                  RunSituationCount_data.para_flowAnaly_static))
    def test_query(self, para):
        """
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        :return:
        """
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RunSituationCount_data.para_flowAnaly,
                                  RunSituationCount_data.para_flowAnaly_static, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)