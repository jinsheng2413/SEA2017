# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_LineDocManage.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.txjx.datamaintain.datamaintain_data import Datamaintain_data
from com.nrtest.sea.pages.adv_app.txjx.datamaintain.lineDocManage_page import LineDocManagePage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→台线系统→资料维护→线路资料维护
@ddt
class TestLineDocManage(TestCase, LineDocManagePage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(Datamaintain_data.lineData_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(DataGatherMan_data.tmnlInstallDetail_tabOne)
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
        # self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 选择变电站
        self.inputSel_subs(para['SUBS'])

        # 输入负责人
        self.inputSel_master(para['MASTER'])

        # 输入线路名称
        self.inputStr_line_name(para['LINE_NAME'])

        # 无负责人
        self.inputChk_no_master(para['NO_MASTER'])

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
    @data(*DataAccess.getCaseData(Datamaintain_data.lineData_para))
    def test_query(self, para):
        """高级应用→台线系统→资料维护→线路资料维护
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(Datamaintain_data.lineData_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
