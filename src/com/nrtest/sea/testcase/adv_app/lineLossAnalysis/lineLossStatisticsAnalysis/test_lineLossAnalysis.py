# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_lineLossAnalysis.py
@time: 2018/10/30 16:26
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossStatisticsAnalysis_data import \
    LineLossStatisticsAnalysis_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossAnalysis_page import \
    LineLossAnalysisPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→线损管理→线损统计分析→线路线损分析
@ddt
class TestLineLossAnalysis(TestCase, LineLossAnalysisPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LineLossStatisticsAnalysis_data.LineLossAnalysis_para)
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
        # 节点名称
        self.openLeftTree(para['TREE_NODE'])

        # 线损率
        self.inputSel_line_loss_rate(para['LINE_LOSS_RATE'])

        # 线损率值
        self.inputStr_line_loss_rate_input(para['LINE_LOSS_RATE_INPUT'])

        if self.get_para_value(para['LINE_LOSS_RATE']).startswith('大于'):
            # 线损率TO
            self.inputSel_line_loss_rate_to(para['LINE_LOSS_RATE_TO'])

            # 线损率TO值
            self.inputStr_line_loss_rate_to_input(para['LINE_LOSS_RATE_TO_INPUT'])

        # 线路编号
        self.inputStr_line_no(para['LINE_NO'])

        # 线路名称
        self.inputStr_line_name(para['LINE_NAME'])

        # 线损类型
        self.inputChk_loss_line_type(para['LOSS_LINE_TYPE'])

        # 按日期类型
        self.inputChk_qry_date_type(para['QRY_DATE_TYPE'])

        qry_date_type = self.get_para_value(para['QRY_DATE_TYPE'])

        if qry_date_type in ('按日', '按月', '按年'):
            # 查询日期
            self.inputDt_query_date(para['QUERY_DATE'])
        elif qry_date_type in ('按时间段', '按周'):
            # 从
            self.inputDt_start_date(para['START_DATE'])

            # 到
            self.inputDt_end_date(para['END_DATE'])
        else:
            # 季度
            self.inputChk_quarter(para['QUARTER'])

        # 组合单元
        self.inputChk_combination_unit(para['COMBINATION_UNIT'])

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
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.LineLossAnalysis_para))
    def test_query(self, para):
        """高级应用→线损管理→线损统计分析→线路线损分析
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.LineLossAnalysis_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
