# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_loadCount.py
@time: 2019/1/30 0030 9:12
@desc:
"""
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.onlyChangeSysthesisQuery_page import LoadCountPage


# 统计查询--综合查询--专公变综合查询：负荷统计
@ddt
class TestLoadCount(TestCase, LoadCountPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SynthQuery_data.onlyChangeSysthesisQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.onlyChangeSysthesisQuery_loadCount_tab)
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
        # 用户编号
        self.openLeftTree(para['TREE_NODE'])
        sleep(1)

        # 终端地址
        self.inputSel_tmnl_addr(para['TMNL_ADDR'])

        # 电能表
        self.inputSel_meter(para['METER'])

        # 数据类型
        self.inputChk_data_type(para['DATA_TYPE'])

        # 日期
        self.inputDt_query_date(para['QUERY_DATE'])

        data_type = self.get_para_value(para['DATA_TYPE'])
        if data_type == '日数据':
            # 瞬时量
            self.inputChk_quantity_type(para['QUANTITY_TYPE'])

            # 积分曲线
            self.inputChk_integral_curve(para['INTEGRAL_CURVE'])

            # 曲线间隔
            self.inputSel_curve_period(para['CURVE_PERIOD'])
        else:
            # 最大最小值分类
            self.inputChk_max_min_type(para['MAX_MIN_TYPE'])

        # 有功
        self.inputChk_power_type(para['POWER_TYPE'])

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
    @data(*DataAccess.getCaseData(SynthQuery_data.onlyChangeSysthesisQuery_para,
                                  SynthQuery_data.onlyChangeSysthesisQuery_loadCount_tab))
    def test_query(self, para):
        """# 统计查询--综合查询--专公变综合查询：负荷统计
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.onlyChangeSysthesisQuery_para,
                                  SynthQuery_data.onlyChangeSysthesisQuery_loadCount_tab, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
