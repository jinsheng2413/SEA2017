# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_distributedEnergyLoadMonitor.py
@time: 2018/11/12 10:33
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyManage_data import \
    DistributedEnergyMange_data
from com.nrtest.sea.pages.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyLoadMonitor_page import \
    DistributedEnergyLoadMonitorPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→重点用户监测→分布式电源管理→分布式电源负荷监测
@ddt
class TestDistributedEnergyLoadMonitor(TestCase, DistributedEnergyLoadMonitorPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(DistributedEnergyMange_data.DistributedEnergyLoadMonitor_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(DistributedEnergyMange_data.DistributedEnergyLoadMonitor_tabName)
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
        self.openLeftTree(para['TREE_NODE'])
        # 统计方式
        self.inputChk_stat_way(para['STAT_WAY'])
        # 日期
        self.inputDt_query_date(para['DATE'])
        # 发电类型
        self.inputSel_elec_type(para['ELEC_TYPE'])
        # 发电量消纳方式
        self.inputSel_abso_type(para['ABSO_TYPE'])
        # 负荷类型
        self.inputChk_load_type(para['LOAD_TYPE'])
        # 查询按钮
        self.btn_search()

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
    @data(
        *DataAccess.getCaseData(DistributedEnergyMange_data.DistributedEnergyLoadMonitor_para,
                                DistributedEnergyMange_data.DistributedEnergyLoadMonitor_tabName))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DistributedEnergyMange_data.DistributedEnergyLoadMonitor_para,
                                  DistributedEnergyMange_data.DistributedEnergyLoadMonitor_tabName, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
