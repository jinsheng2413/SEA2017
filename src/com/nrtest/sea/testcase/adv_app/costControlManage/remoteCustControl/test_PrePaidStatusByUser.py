# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_PrePaidStatusByUser.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.remoteCustControl.remoteCustControl_data import \
    RemoteCustControl_data
from com.nrtest.sea.pages.adv_app.costControlManage.remoteCustControl.PrePaidStatus_page import \
    PrePaidStatusByUserPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→费控管理→远程费控→远程费控执行统计:按用户执行统计
@ddt
class TestPrePaidStatusByUser(TestCase, PrePaidStatusByUserPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(RemoteCustControl_data.prePaidStatus_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(RemoteCustControl_data.NewTab_ByUser)
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
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 控制类型
        self.inputSel_ctrl_type(para['CTRL_TYPE'])

        # 开始时间
        self.inputDt_start_time(para['START_TIME'])

        # 结束时间
        self.inputDt_end_time(para['END_TIME'])

        # 查询
        self.btn_qry()
        self.sleep_time(2)

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
    @data(*DataAccess.getCaseData(RemoteCustControl_data.prePaidStatus_para, RemoteCustControl_data.NewTab_ByUser))
    def test_userQuery(self, para):
        """高级应用→费控管理→远程费控→远程费控执行统计:按用户执行统计

        :param para:
        """
        self.query(para)
        self.start_case(para, __file__)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RemoteCustControl_data.prePaidStatus_para, RemoteCustControl_data.NewTab_ByUser, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()