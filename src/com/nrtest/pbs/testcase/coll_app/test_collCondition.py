# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_collCondition.py
@time: 2019-07-08 16:50
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.pbs.data.coll_app.collOperMain_data import CollOperMain_data
from com.nrtest.pbs.page.coll_app.collCondition_page import CollConditionPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 采集运维→采集工况
@ddt
class TestCollCondition(TestCase, CollConditionPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(CollOperMain_data.collCondition_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        cls.goto_frame(cls)
        # menuPage.clickTabPage()
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        cls.goto_home_page(cls)


    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        # self.closeLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 数据中断时间超过
        self.inputSel_time_out(para['TIME_OUT'])
        # 电压等级
        self.inputSel_vol_level(para['VOL_LEVEL'])
        # 查询按钮
        self.btn_qry()



    def assert_query_result(self, para):
        """
        查询结果校验
        :param para:
        """
        # self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CollOperMain_data.collCondition_para))
    def test_query(self, para):
        """采集运维→采集工况
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CollOperMain_data.collCondition_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
