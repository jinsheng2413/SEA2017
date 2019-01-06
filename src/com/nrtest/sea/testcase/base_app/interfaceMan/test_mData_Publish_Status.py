# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_mData_Publish_Status.py
@time: 2018-09-21 10:47
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.mDataPublishStatus_data import MDataPublishStatus_data
from com.nrtest.sea.pages.base_app.interfaceMan.mDataPublishStatus_page import MDataPublishStatusPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


@ddt
class Test_mData_Publish_StatusPage(TestCase, MDataPublishStatusPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(MDataPublishStatus_data.para_MDataPublishStatus)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(MDataPublishStatus_data.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

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
        # self.recoverLeftTree()

    def query(self, para):
        # 选择业务系统
        self.inputSel_BusinessSystem(para['BUSINESS_SYSTEM'])
        # 开始时间
        self.inputDt_receive_time(para['START_DATE'])
        # 结束时间
        self.inputDt_end_time(para['END_DATE'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(MDataPublishStatus_locators.TAB_ONE)
        # self.assertTrue(result)

    # @data(*DataAccess.getCaseData(MDataPublishStatus_data.para_MDataPublishStatus))
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
    @data(*DataAccess.getCaseData(MDataPublishStatus_data.para_MDataPublishStatus))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(MDataPublishStatus_data.para_MDataPublishStatus, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
