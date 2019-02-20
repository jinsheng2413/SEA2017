# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_NewRemoteCtrlExecut_low_info.py
@time: 2019-02-20 09:35:53
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.remoteCustControl.remoteCustControl_data import \
    RemoteCustControl_data
from com.nrtest.sea.pages.adv_app.costControlManage.remoteCustControl.newRemoteCtrlExecut_page import \
    NewRemoteCtrlExecu_low_info_Page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→费控管理→远程费控→新低压用户远程费控执行:低压用户费控汇总信息
@ddt
class test_NewRemoteCtrlExecutLow_info(TestCase, NewRemoteCtrlExecu_low_info_Page):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(RemoteCustControl_data.para_NewRemoteCtrlExecut)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(RemoteCustControl_data.para_NewRemoteCtrlExecut_low_info)
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
        # 催费控制批次号
        self.inputStr_control_order_no(para['CONTROL_ORDER_NO'])

        # 签发开始时间
        self.inputDt_start_type(para['START_TYPE'])

        # 签发结束时间
        self.inputDt_end_date(para['END_DATE'])

        # 营销U1验签结果
        self.inputSel_u1_result(para['U1_RESULT'])

        # 统计类型
        self.inputChk_stat_type(para['STAT_TYPE'])

        # 查询
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
    @data(*DataAccess.getCaseData(RemoteCustControl_data.para_NewRemoteCtrlExecut,
                                  RemoteCustControl_data.para_NewRemoteCtrlExecut_low_info))
    def test_query(self, para):
        """高级应用→费控管理→远程费控→新低压用户远程费控执行:低压用户费控汇总信息
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RemoteCustControl_data.para_NewRemoteCtrlExecut,
                                  RemoteCustControl_data.para_NewRemoteCtrlExecut_low_info, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
