# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_elePricePara.py
@time: 2018/8/16 0016 8:55
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.localCostControl.localCostControl_para import LocalCostContral_data
from com.nrtest.sea.pages.adv_app.costControlManage.elePricePara_page import ElePricePages
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→费控管理→本地费控→电价参数下发
@ddt
class TestElePricePara(TestCase, ElePricePages):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(LocalCostContral_data.elePricePara_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
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
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 工单编号
        self.inputStr_app_no(para['APP_NO'])

        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])

        # 接收时间
        self.inputDt_receive_date(para['RECEIVE_DATE'])

        # 执行状态
        self.inputSel_execute_status(para['EXECUTE_STATUS'])

        # 终端地址
        self.inputStr_terminal_addr(para['TERMINAL_ADDR'])

        # 电表地址
        self.inputStr_meter_addr(para['METER_ADDR'])

        # 抄表段号
        self.inputStr_mr_sect_no(para['MR_SECT_NO'])

        # 结束时间
        self.inputDt_end_date(para['END_DATE'])

        # 任务类型
        self.inputSel_task_type(para['TASK_TYPE'])

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
    @data(*DataAccess.getCaseData(LocalCostContral_data.elePricePara_para))
    def test_query(self, para):
        """高级应用→费控管理→本地费控→电价参数下发
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LocalCostContral_data.elePricePara_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
