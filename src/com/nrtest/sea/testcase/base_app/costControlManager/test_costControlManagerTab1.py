# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_costControlManagerTab1.py
@time: 2019-02-13 15:59:42
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.remoteCustControl.remoteCustControl_data import \
    RemoteCustControl_data
from com.nrtest.sea.pages.base_app.costControlManager.costControlManager_page import NewSpecRemoteCtrlExecutPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→费控管理→远程费控→新专变用户远程费控执行:高压用户跳闸控制列表
@ddt
class TestNewSpecRemoteCtrlExecutTab1(TestCase, NewSpecRemoteCtrlExecutPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(RemoteCustControl_data.para_NewSpecRemoteCtrlExecut)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(RemoteCustControl_data.para_NewSpecRemoteCtrlExecut_high_sheet)
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

        # 催费控制批次号
        self.inputStr_control_order_no(para['CONTROL_ORDER_NO'])

        # 采集点编号
        self.inputStr_cp_no(para['CP_NO'])

        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])

        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])

        # 终端资产号
        self.inputStr_tmnl_asst_no(para['TMNL_ASST_NO'])

        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])

        # 控制类别
        self.inputSel_control_type(para['CONTROL_TYPE'])

        # 工单状态
        self.inputSel_app_status(para['APP_STATUS'])

        # 密文比对结果
        self.inputSel_compare_result(para['COMPARE_RESULT'])

        # 统计类型
        self.inputChk_stat_type(para['STAT_TYPE'])

        # 签发开始时间
        self.inputDt_start_date(para['START_DATE'])

        # 签发结束时间
        self.inputDt_end_date(para['END_DATE'])

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
    @data(*DataAccess.getCaseData(RemoteCustControl_data.para_NewSpecRemoteCtrlExecut,
                                  RemoteCustControl_data.para_NewSpecRemoteCtrlExecut_high_sheet))
    def test_query(self, para):
        """高级应用→费控管理→远程费控→新专变用户远程费控执行:高压用户跳闸控制列表
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RemoteCustControl_data.para_NewSpecRemoteCtrlExecut,
                                  RemoteCustControl_data.para_NewSpecRemoteCtrlExecut_high_sheet, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
