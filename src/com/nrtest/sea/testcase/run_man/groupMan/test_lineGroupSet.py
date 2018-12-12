# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_lineGroupSet.py
@time: 2018/11/12 16:25
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.groupMan.groupMan_data import GroupMan_data
from com.nrtest.sea.pages.run_man.groupMan.lineGroupSet_page import *
from com.nrtest.sea.task.commonMath import *


# 运行管理→群组管理→线路群组设置
@ddt
class TestLineGroupSet(unittest.TestCase, LineGroupSetPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GroupMan_data.LineGroupSet_para, True)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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

        # sleep(2)
        self.clickRadioBox(para['TAB_PAGE_SEL'])  # '管理群组')
        sleep(0.5)
        if para['TAB_PAGE_SEL'] == '管理群组':
            # 名称
            self.inputStr_name(para['NAME'])

            # 有效日期
            self.clickSingleCheckBox(para['VALID_DT'])

            if len(para['VALID_DT']) > 0:
                # 查询日期，开始【少个“从”的标签】
                self.inputDt_start_date(para['START_DATE'])
                # 查询日期，结束
                self.inputDt_end_date(para['END_DATE'])
                # 查询按钮
                self.btn_search()

    #     # 校验
    #     result = self.assert_context(*LineGroupSetLocators.CHECK_FIRST)
    #     self.assertTrue(result)
    #
    # @BeautifulReport.add_test_img()
    # @data(*DataAccess.getCaseData(GroupMan_data.LineGroupSet_para))
    # def test_der(self, para):
    #     self.query(para)

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
    @data(*DataAccess.getCaseData(GroupMan_data.LineGroupSet_para))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        if para['TAB_PAGE_SEL'] == '管理群组':
            self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GroupMan_data.LineGroupSet_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        if para['TAB_PAGE_SEL'] == '管理群组':
            self.assert_query_criteria(para)
        self.end_case(para)
