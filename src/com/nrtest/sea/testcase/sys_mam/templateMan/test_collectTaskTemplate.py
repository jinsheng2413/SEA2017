# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_collectTaskTemplate.py
@time: 2018/11/21 9:53
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.templateMan.templateMan_data import TemplateManData
from com.nrtest.sea.pages.sys_mam.templateMan.collectTaskTemplate_page import CollectTaskTemplatePage, \
    CollectTaskTemplateLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→模板管理→采集任务模板
@ddt
class TestCollectTaskTemplate(unittest.TestCase, CollectTaskTemplatePage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(TemplateManData.CollectTaskTemplate_para)

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
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 任务分类
        self.inputSel_task_classify(para['TASK_CLASSIFY'])
        # 任务类型
        self.inputSel_task_type(para['TASK_TYPE'])
        # 模板名称
        self.inputStr_template_name(para['TEMPLATE_NAME'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*CollectTaskTemplateLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(TemplateManData.CollectTaskTemplate_para))
    def test_der(self, para):
        self.query(para)
