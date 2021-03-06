# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_meterStateArr.py
@time: 2019-02-19 08:56:34
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.meterMan.meterClockMan_data import MeterClockMan_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.meterMan.meterStateArr_page import MeterStateArrPage


# 运行管理→电能表管理→电能表状态维护(蒙东)
@ddt
class TestMeterStateArr(TestCase, MeterStateArrPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(MeterClockMan_data.meterStateArr_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage()
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 关闭菜单页面
        cls.closePages(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        每个测试用例测试结束后的操作，在这里做相关清理工作
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
        # 供电单位
        self.openLeftTree(para['TREE_NODE'])

        # 终端状态
        self.inputSel_tmnl_status(para['TMNL_STATUS'])

        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])

        # 终端地址
        self.inputStr_terminal_addr(para['TERMINAL_ADDR'])

        # 包含下级供电单位
        self.inputChk_contain_org(para['CONTAIN_ORG'])

        # 查询
        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(MeterClockMan_data.meterStateArr_para))
    def test_query(self, para):
        """运行管理→电能表管理→电能表状态维护(蒙东)
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(MeterClockMan_data.meterStateArr_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
