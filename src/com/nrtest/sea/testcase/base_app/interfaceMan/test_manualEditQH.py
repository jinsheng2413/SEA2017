# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_manualEditQH.py
@time: 2018-11-07 16:37
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.manualEditQH_data import InterfaceManager_data
from com.nrtest.sea.pages.base_app.interfaceMan.manualEditQH_page import ManualEditQH_Locators, ManualEditQHPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用--接口管理--人工补录(青海)
@ddt
class Test_ManualEditQH(TestCase, ManualEditQHPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(InterfaceManager_data.para_ManualEditQH)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(InterfaceManager_data.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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

    def query(self, para):
        # 打开左边树选择供电单位
        self.openLeftTree(para['TREE_NODE'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 数据来源
        self.inputSel_data_from(para['DATA_FROM'])
        # 日期
        self.inputDt_query_date(para['QUERY_DATE'])
        # 点击正向有功总为空
        self.click(ManualEditQH_Locators.QRY_IS_EMPTY)
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        # result = self.assert_context(ManualEditQH_Locators.TAB_ONE)
        # self.assertTrue(result)

    # @BeautifulReport.add_test_img()
    # @data(*DataAccess.getCaseData(InterfaceManager_data.para_ManualEditQH))
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
    @data(*DataAccess.getCaseData(InterfaceManager_data.para_ManualEditQH))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(InterfaceManager_data.para_ManualEditQH, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
