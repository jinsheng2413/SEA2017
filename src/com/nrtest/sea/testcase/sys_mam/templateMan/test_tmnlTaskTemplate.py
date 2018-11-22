# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_tmnlTaskTemplate.py
@time: 2018/11/21 14:42
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.templateMan.templateMan_data import TemplateManData
from com.nrtest.sea.pages.sys_mam.templateMan.tmnlTaskTemplate_page import TmnlTaskTemplatePage, \
    TmnlTaskTemplateLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→模板管理→终端任务模板
@ddt
class TestTmnlTaskTemplate(unittest.TestCase, TmnlTaskTemplatePage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            TemplateManData.TmnlTaskTemplate_para, True)

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
        # 任务状态
        self.inputSel_task_stat(para['TASK_STAT'])
        # 方案类型
        self.inputSel_scheme_type(para['SCHEME_TYPE'])
        # 执行优先级
        self.inputSel_execution_priority(para['EXECUTION_PRIORITY'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*TmnlTaskTemplateLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(TemplateManData.TmnlTaskTemplate_para))
    def test_der(self, para):
        self.query(para)
