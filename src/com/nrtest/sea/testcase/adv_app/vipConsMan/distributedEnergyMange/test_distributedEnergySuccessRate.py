# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_distributedEnergySuccessRate.py
@time: 2018/11/9 9:25
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyManage_data import \
    DistributedEnergyMange_data
from com.nrtest.sea.pages.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyMonitor_page import \
    DistributedEnergySuccessRatePage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测:分布式电源采集成功率
@ddt
class TestDistributedEnergySuccessRate(TestCase, DistributedEnergySuccessRatePage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(DistributedEnergyMange_data.DistributedEnergyMonitor_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(DistributedEnergyMange_data.DistributedEnergyMonitor_tabName_Success)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

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
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'], is_closed=True)
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 开始日期
        self.inputDt_start_date(para['START_DATE'])
        # 结束日期
        self.inputDt_end_date(para['END_DATE'])
        # 查询按钮
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
    @data(*DataAccess.getCaseData(DistributedEnergyMange_data.DistributedEnergyMonitor_para,
                                  DistributedEnergyMange_data.DistributedEnergyMonitor_tabName_Success))
    def test_query(self, para):
        """高级应用→重点用户监测→分布式电源管理→分布式电源采集监测:分布式电源采集成功率
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DistributedEnergyMange_data.DistributedEnergyMonitor_para,
                                  DistributedEnergyMange_data.DistributedEnergyMonitor_tabName_Success, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
