# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_f35SetCollTaskTemp.py
@time: 2018/11/21 15:11
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.templateMan.templateMan_data import TemplateManData
from com.nrtest.sea.pages.sys_mam.templateMan.f35SetCollTaskTemp_page import F35SetCollTaskTempPage
from com.nrtest.sea.task.commonMath import *


# 系统管理→模板管理→F35设置采集任务模板
@ddt
class TestF35SetCollTaskTemp(unittest.TestCase, F35SetCollTaskTempPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # # 打开菜单（需要传入对应的菜单编号）
        # cls.driver = openMenu(TemplateManData.F35SetCollTaskTemp_para)
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(TemplateManData.F35SetCollTaskTemp_para)
        super(unittest.TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(SysConfigManData.SysAbnormalParaSet_tabName)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

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
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 任务分类
        self.inputSel_task_classify(para['TASK_CLASSIFY'])
        # 任务类型
        self.inputSel_task_type(para['TASK_TYPE'])
        # 模板名称
        self.inputStr_template_name(para['TEMPLATE_NAME'])
        # 查询按钮
        self.btn_search()
        sleep(2)

    #     # 校验
    #     result = self.assert_context(F35SetCollTaskTempLocators.CHECK_FIRST)
    #     self.assertTrue(result)
    #
    # @BeautifulReport.add_test_img()
    # @data(
    #     *DataAccess.getCaseData(TemplateManData.F35SetCollTaskTemp_para))
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
    @data(*DataAccess.getCaseData(TemplateManData.F35SetCollTaskTemp_para))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TemplateManData.F35SetCollTaskTemp_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
