# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_lineLossStatisticsQuery.py
@time: 2018/10/31 14:52
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossStatisticsAnalysis_data import \
    LineLossStatisticsAnalysis_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossStatisticsQuery_page import \
    LineLossStatisticsQueryPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→线损分析→线损统计分析→线损统计查询
@ddt
class TestLineLossStatisticsQuery(TestCase, LineLossStatisticsQueryPage):

    @classmethod
    def setUpClass(cls):

        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LineLossStatisticsAnalysis_data.LineLossStatisticsQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
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
        # 线损分类
        self.inputSel_line_loss_type(para['LINE_LOSS_TYPE'])
        # 线损率
        self.inputSel_line_loss_rate(para['LINE_LOSS_RATE'])
        # 线损率值
        self.inputStr_line_loss_rate(para['LINE_LOSS_RATE_INPUT'])
        # 日期类型
        self.inputChk_qry_date_type(para['QRY_DATE_TYPE'])

        qry_date_type = self.get_para_value(para['QRY_DATE_TYPE'])
        if qry_date_type == '日':
            self.inputDt_query_date(para['QUERY_DATE'])
        else:
            self.inputDt_start_date(para['START_DATE'])
            self.sleep_time(0.5)
            self.inputDt_end_date(para['END_DATE'])

        # if para['QRY_DATE_TYPE'].count('日') > 2:
        #     self.inputChl_qry_type(para['QRY_TYPE'])
        #     # 日期
        #     self.inputDt_query_date(para['QUERY_DATE'])
        # elif para['QRY_TYPE_MONTH'].count('月') > 2:
        #     self.inputChl_qry_type_month(para['QRY_TYPE_MONTH'])
        #     self.inputDt_start_date(para['FROM'])
        #     self.sleep_time(2)
        #     self.inputDt_end_date(para['END_DATE'])
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
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.LineLossStatisticsQuery_para))
    def test_query(self, para):
        """高级应用→线损分析→线损统计分析→线损统计查询

        :param para:
        """
        print(para)
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.LineLossStatisticsQuery_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
