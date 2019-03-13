# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_zoneAreaSameGoodStandard.py
@time: 2019/1/28 0028 14:31
@desc:
"""
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.ld_system.lineLossCount.linelossCount_data import LineLossCount_data
from com.nrtest.sea.pages.adv_app.ld_system.lineLossCount.zoneAreaSameGoodStandard_page import \
    ZoneAreaSameGoodStandard_page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用 → 台线系统 →线损统计 →台区同期月优秀达标查询
@ddt
class TestRecordsQuery(TestCase, ZoneAreaSameGoodStandard_page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LineLossCount_data.lineLossCount_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(IntelligentLock_data.RecordsQuery_tabName_asset)
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
        sleep(2)
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 选择人员
        self.inputSel_select_person(para['SELECT_PERSON'])
        # 开始时间
        self.inputDt_start_date(para['START_DATE'])
        # 结束日期
        self.inputDt_end_date(para['END_DATE'])

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
    @data(*DataAccess.getCaseData(LineLossCount_data.lineLossCount_para))
    def test_query(self, para):
        """# 高级应用→台线系统→线损统计→台区同期月优秀达标查询
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(LineLossCount_data.lineLossCount_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
