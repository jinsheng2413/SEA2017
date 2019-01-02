# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_assessmentParameterSetting.py
@time: 2018/11/1 9:34
@desc:
"""

import unittest
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossIndexEvaluation.lineLossIndexEvaluation_data import \
    LineLossIndexEvaluation_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossIndexEvaluation.assessmentParameterSetting_page import \
    AssessmentParameterSettingPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→线损指标考核→考核参数设置
@ddt
class TestAssessmentParameterSetting(unittest.TestCase, AssessmentParameterSettingPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LineLossIndexEvaluation_data.AssessmentParameterSetting_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)


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
        print(para)
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 台区/线路名称
        self.inputStr_tg_name(para['TG_NAME'])
        # 记录形式
        print(para['RECORDER_MANAGER'])

        if '已录入管理员' in para['RECORDER_MANAGER']:
            sleep(2)
            self.inputChk_recorderModel(para['RECORDER_MANAGER'])
        else:
            self.inputChk_recorderModel(para['UNRECORDER_MANAGER'])
        # 查询按钮
        self.btn_search()

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

    # @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossIndexEvaluation_data.AssessmentParameterSetting_para))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossIndexEvaluation_data.AssessmentParameterSetting_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
