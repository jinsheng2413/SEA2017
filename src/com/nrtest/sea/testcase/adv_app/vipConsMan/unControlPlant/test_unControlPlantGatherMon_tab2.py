# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_unControlPlantGatherMon_tab2.py
@time: 2018-11-07 10:17
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_data import UnControlPlant
from com.nrtest.sea.pages.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_page import \
    UnControlPlantGatherMon2_Page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用--重点用户监测--非统调电厂管理--非统调电厂采集监测：高级应用→重点用户监测--非统调电厂管理--非统调电厂采集监测：非统调电厂采集监测明细
@ddt
class Test_UnControlPlantGatherMon_2(TestCase, UnControlPlantGatherMon2_Page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(UnControlPlant.para_unControlPlantGatherMon)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(UnControlPlant.para_unControlPlantGatherMon_tab_detail)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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

        # 发电方式
        self.inputSel_gc_type(para['GC_TYPE'])

        # 采集方式
        self.inputSel_coll_mode(para['COLL_MODE'])

        # 查询日期
        self.inputDt_query_date(para['QUERY_DATE'])

        # 户号
        self.inputStr_cons_no(para['CONS_NO'])

        # 表资产编号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])

        # 终端资产号
        self.inputStr_tmnl_asset_no(para['TMNL_ASSET_NO'])

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
    @data(*DataAccess.getCaseData(UnControlPlant.para_unControlPlantGatherMon,
                                  UnControlPlant.para_unControlPlantGatherMon_tab_detail))
    def test_query(self, para):
        """高级应用--重点用户监测--非统调电厂管理--非统调电厂采集监测：高级应用→重点用户监测--非统调电厂管理--非统调电厂采集监测：非统调电厂采集监测明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(UnControlPlant.para_unControlPlantGatherMon,
                                  UnControlPlant.para_unControlPlantGatherMon_tab_detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
