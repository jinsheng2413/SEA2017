# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_CtrlExecut.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.custMan.custMan_data import CustMan_data
from com.nrtest.sea.pages.base_app.custMan.ctrlExecutPage import CtrlExecutPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→费控管理→远程费控→低压用户远程费控执行
@ddt
class TestCtrlExecut(TestCase, CtrlExecutPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(CustMan_data.ctrlExecut_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(CustMan_data.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭菜单
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
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(CtrlExecutPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])

        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])

        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])

        # 控制类型
        self.inputSel_ctrl_type(para['CTRL_TYPE'])

        # 抄表段号
        self.inputStr_mr_sect_no(para['MR_SECT_NO'])

        # 执行状态
        self.inputSel_execute_status(para['EXECUTE_STATUS'])

        # 数据来源
        self.inputSel_data_src(para['DATA_SRC'])

        # 确认状态
        self.inputSel_confirm_status(para['CONFIRM_STATUS'])

        # 时间区间
        self.inputChk_dt_interal(para['DT_INTERAL'])

        # 开始时间
        self.inputDt_start_time(para['START_TIME'])

        # 结束时间
        self.inputDt_end_time(para['END_TIME'])

        # 工单号
        self.inputStr_app_no(para['APP_NO'])

        # 执行结果状态
        self.inputSel_exe_result_status(para['EXE_RESULT_STATUS'])

        # 查询
        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验
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
    @data(*DataAccess.getCaseData(CustMan_data.ctrlExecut_para))
    def test_query(self, para):
        """高级应用→费控管理→远程费控→低压用户远程费控执行
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CustMan_data.ctrlExecut_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
