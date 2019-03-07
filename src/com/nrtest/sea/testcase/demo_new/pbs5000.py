# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: pbs5000.py
@time: 2019/01/08 16:41
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.pbs.page.countFormula_page import CountFormula_page
from com.nrtest.pbs.tree.tree_page import *
from com.nrtest.sea.pages.other.menu_page import MenuPage

count_formula = '0000103'
@ddt
class TestPBS5000(TestCase, CountFormula_page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(count_formula)  # 厂站设备--30
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)


    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        # cls.closePages(cls)
        # cls.goto_home_iframe(cls)
        cls.main_page(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.closeLeftTree()
    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        self.into_iframe()

        # 打开左边树并选择
        self.openLeftTree(Page['TREE_NODE'])
        # 公式名
        self.inputStr_formula_name(para['FORMULA_NAME'])
        #公式别名
        self.inputStr_formula_alias(para['FORMULA_ALIAS'])
        #计算时间间隔
        self.inoutSel_conputer_Interval(para["COMPUTER_NITERVAL"])
        #所属对象
        # self.inputStr_object(para['AFFILIATION_OBJECT'])
        #分时时标
        self.inputStr_minute_scale(para["MINUTES_TIME_SCALE"])
        #日时间
        self.inputStr_day_time(para['DAY_TIME'])
        #约时间
        self.inputStr_month_time(para["MONTH_TIME"])
        #公式类型
        self.inoutSel_formula_type(para['FORMULA_TYPE'])
        self.btn_qry()


        self.iframe_back(num=1)

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
    @data(*DataAccess.getCaseData('0000103'))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(count_formula, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()



