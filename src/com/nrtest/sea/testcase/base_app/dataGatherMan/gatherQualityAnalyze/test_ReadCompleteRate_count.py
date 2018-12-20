# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.GatherQualityAnalyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.ReadCompleteRate_page import ReadCompleteRatePage, \
    ReadCompleteRateLocators
from com.nrtest.sea.task.commonMath import *

ReadCompleteRatePage


@ddt
class TestReadCompleteRate(unittest.TestCase, ReadCompleteRatePage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GatherQualityAnalyze_data.readCompleteRate_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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

    def countQuery(self, para):
        clickTabPage(para['TAB_NAME'])
        self.exec_script(ReadCompleteRateLocators.JS_COUNT)
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 用户类型
        self.inputSel_userType_count(para['USER_TYPE'])
        # 通信方式
        self.inputSel_communicationModeCount(para['COMMNUCATION_MODE'])
        # 终端厂家
        self.inputSel_tmnlFactoryCount(para['TMNL_FACTORY'])
        # 蕊片厂家
        self.inputSel_chipFactoryCount(para['CHIP_FACTORY'])

        # 日期时间
        self.inputStr_date_time_count(para['DATE_TIME'])
        self.btn_count_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ReadCompleteRateLocators.TAB_COUNT_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.readCompleteRate_para,
                                  GatherQualityAnalyze_data.readCompleteRateCount_tab))
    def test_countQuery(self, para):
        self.countQuery(para)
