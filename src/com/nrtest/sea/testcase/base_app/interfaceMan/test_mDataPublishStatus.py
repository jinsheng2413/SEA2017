# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_mDataPublishStatus.py
@time: 2018-10-30 16:10
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.mDataPublishStatus2_data import InterfaceManager_data
from com.nrtest.sea.pages.base_app.interfaceMan.mDataPublishStatus2_page import MDataPublishStatus2Page
from com.nrtest.sea.task.commonMath import *


# 基本应用--接口管理--营销业务接口--数据发布情况
@ddt
class Test_mDataPublishStatus2(unittest.TestCase, MDataPublishStatus2Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # cls.driver = openMenu(InterfaceManager_data.para_MDataPublishStatus2)
        # sleep(2)
        # cls.exec_script(cls, MDataPublishStatus2_locators.START_DATE_JS)
        # cls.exec_script(cls, MDataPublishStatus2_locators.END_DATE_JS)
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(InterfaceManager_data.para_MDataPublishStatus2)
        super(unittest.TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(SysConfigManData.SysAbnormalParaSet_tabName)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        self.inputSel_BusinessSystem(para['BUSINESS_SYSTEM'])
        # 开始时间
        self.inputStr_receive_time(para['START_DATE'])
        # 结束时间
        self.inputStr_end_time(para['END_DATE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)

    #     # 校验
    #     result = self.assert_context(MDataPublishStatus2_locators.TAB_ONE)
    #     self.assertTrue(result)
    #
    # @data(*DataAccess.getCaseData(InterfaceManager_data.para_MDataPublishStatus2))
    # def test_query(self, para):
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
    @data(*DataAccess.getCaseData(InterfaceManager_data.para_MDataPublishStatus2))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(InterfaceManager_data.para_MDataPublishStatus2, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
