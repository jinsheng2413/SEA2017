# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_loseCountPowerMan.py
@time: 2018/11/2 0002 9:05
@desc:
"""
import unittest
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossMantain.lineLossMantain_data import LineLossMantain_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossMantain.loseCountPowerMan_page import LoseCountPowerManPage
from com.nrtest.sea.task.commonMath import *


# 高级应用-->线损分析--》线损模型维护--》线损计算模型管理
@ddt
class TestLoseCountPowerMan(unittest.TestCase, LoseCountPowerManPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LineLossMantain_data.loseCountPowerMan_para)
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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 台区运行状态
        self.inputSel_zoneAreaRunStatus(para['ZONE_AREA_RUN_STATUS'])
        # 台区编码
        self.inputStr_zoneAreaCode(para['ZONE_AREA_CODE'])
        # 台区名称
        self.inputStr_zoneAreaName(para['ZONE_AREA_NAME'])
        # 责任人人工号
        self.inputStr_responsibilierNo(para['RESPONSIBLLIER_NO'])

        self.btn_qry()

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
    @data(*DataAccess.getCaseData(LineLossMantain_data.loseCountPowerMan_para))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossMantain_data.loseCountPowerMan_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
