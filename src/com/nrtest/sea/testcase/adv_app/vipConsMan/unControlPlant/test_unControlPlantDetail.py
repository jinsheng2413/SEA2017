# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_unControlPlantDetail.py
@time: 2018/11/12 11:33
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_data import UnControlPlant
from com.nrtest.sea.pages.adv_app.vipConsMan.unControlPlant.unControlPlantStat_page import \
    UnControlPlantDetailPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→重点用户监测→非统调电厂管理→非统调电厂接入统计→非统调电厂接入明细
@ddt
class TestUnControlPlantDetail(TestCase, UnControlPlantDetailPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(UnControlPlant.UnControlPlantStat_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(UnControlPlant.UnControlPlantStat_tabName_Detail)
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
        # 发电方式
        self.inputSel_elec_way(para['ELEC_WAY'])
        # 采集方式
        self.inputSel_gather_way(para['GATHER_WAY'])
        # 统计日期
        self.inputDt_date(para['DATE'])
        # 户号
        self.inputStr_cons_no(para['CONS_NO'])
        # 表资产编号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 终端资产编号
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 查询按钮
        self.btn_search()

    def assert_query_result(self, para):
        """
        查询结果校验
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
    @data(*DataAccess.getCaseData(UnControlPlant.UnControlPlantStat_para,
                                  UnControlPlant.UnControlPlantStat_tabName_Detail))
    def test_query(self, para):
        """
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        :return:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(UnControlPlant.UnControlPlantStat_para,
                                  UnControlPlant.UnControlPlantStat_tabName_Detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
