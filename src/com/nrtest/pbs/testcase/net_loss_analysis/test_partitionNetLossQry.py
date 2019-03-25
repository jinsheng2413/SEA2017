# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_partitionNetLossQry.py
@time: 2019-03-15 14:25
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.pbs.data.net_loss_analysis.netLossAnalysis_data import NetLossAnalysis_data
from com.nrtest.pbs.page.net_loss_analysis.partitionNetLossQry_page import PartitionNetLossQryPage
from com.nrtest.pbs.tree.tree_page import *
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 网损分析→分区网损查询:网损查询
@ddt
class TestPartitionNetLossQry(TestCase, PartitionNetLossQryPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(NetLossAnalysis_data.partitionNetLossQry_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        cls.goto_frame(cls)
        menuPage.clickTabPage(NetLossAnalysis_data.partitionNetLossQry_tab_qry)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

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

        # 区域
        self.inputSel_area(para['AREA'])
        # 时间方案
        self.inputChk_date_type(para['DATE_TYPE'])
        # 开始时间
        self.inputDt_start_date(para['START_DATE'])
        # 结束时间
        self.inputDt_end_date(para['END_DATE'])
        # TAB页名称
        self.inputChk_tab_name(para['TAB_NAME'])
        # 查询按钮
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
    @data(*DataAccess.getCaseData(NetLossAnalysis_data.partitionNetLossQry_para,
                                  NetLossAnalysis_data.partitionNetLossQry_tab_qry))
    def test_query(self, para):
        """网损分析→分区网损查询:网损查询
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(NetLossAnalysis_data.partitionNetLossQry_para,
                                  NetLossAnalysis_data.partitionNetLossQry_tab_qry, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
