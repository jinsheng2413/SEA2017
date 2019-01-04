# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_runMeterStatistics_detail.py
@time: 2018/10/25 15:26
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.collConstructStatus.collConstructStatus_data import CollConstructStatus_data
from com.nrtest.sea.pages.stat_rey.collConstructStatus.runMeterStatistics_page import RunMeterStatisticsPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→采集建设情况→运行电能表统计→运行电能表明细
@ddt
class TestRunMeterStatistics_Detail(TestCase, RunMeterStatisticsPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(CollConstructStatus_data.RunMeterStatistics_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(CollConstructStatus_data.RunMeterStatistics_tabName_detail)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

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
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 用户类型
        self.inputSel_detail_cons_type(para['DETAIL_CONS_TYPE'])
        # 通信方式
        self.inputSel_detail_tmnl_way(para['DETAIL_TMNL_WAY'])
        # 通讯规约
        self.inputSel_detail_tmnl_protocol(para['DETAIL_TMNL_PROTOCOL'])
        # 设备类型
        self.inputSel_detail_device_type(para['DETAIL_DEVICE_TYPE'])
        # 电能表厂家
        self.inputSel_detail_meter_factory(para['DETAIL_METER_FACTORY'])
        # 电能表状态
        self.inputSel_detail_meter_ststus(para['DETAIL_METER_STATUS'])
        # 查询按钮
        self.btn_detail_search()

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
    @data(*DataAccess.getCaseData(CollConstructStatus_data.RunMeterStatistics_para,
                                  CollConstructStatus_data.RunMeterStatistics_tabName_detail))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CollConstructStatus_data.RunMeterStatistics_para,
                                  CollConstructStatus_data.RunMeterStatistics_tabName_detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
