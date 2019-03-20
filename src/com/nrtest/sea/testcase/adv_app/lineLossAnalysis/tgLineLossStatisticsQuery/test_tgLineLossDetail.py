# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_tgLineLossDetail.py
@time: 2018/11/2 10:15
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossStatisticsQuery_data import \
    TgLineLossStatisticsQuery_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossDetail_page import \
    TgLineLossDetailPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→线损分析→台区线损统计查询→台区线损明细
@ddt
class TestTgLineLossDetail(TestCase, TgLineLossDetailPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(TgLineLossStatisticsQuery_data.TgLineLossDetail_para)
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

        # 采集覆盖率
        self.inputSel_collect_cover_rate(para['COLLECT_COVER_RATE'])

        # 采集覆盖率值
        self.inputStr_collect_cover_rate_input(para['COLLECT_COVER_RATE_INPUT'])

        # 采集成功率
        self.inputSel_collect_success_rate(para['COLLECT_SUCCESS_RATE'])

        # 采集成功率值
        self.inputStr_collect_success_rate_input(para['COLLECT_SUCCESS_RATE_INPUT'])

        # 同期线损率
        self.inputSel_collecline_loss_rate(para['COLLECLINE_LOSS_RATE'])

        # 同期线损率值
        self.inputStr_collecline_loss_rate_input(para['COLLECLINE_LOSS_RATE_INPUT'])

        if self.get_para_value(para['COLLECT_COVER_RATE']).startswith('大于'):
            # 采集覆盖率TO
            self.inputSel_collect_cover_rate_to(para['COLLECT_COVER_RATE_TO'])

            # 采集覆盖率TO值
            self.inputStr_collect_cover_rate_to_input(para['COLLECT_COVER_RATE_TO_INPUT'])

        if self.get_para_value(para['COLLECT_SUCCESS_RATE']).startswith('大于'):
            # 采集成功率TO
            self.inputSel_collect_success_rate_to(para['COLLECT_SUCCESS_RATE_TO'])

            # 采集成功率TO值
            self.inputStr_collect_success_rate_to_input(para['COLLECT_SUCCESS_RATE_TO_INPUT'])

        if self.get_para_value(para['COLLECLINE_LOSS_RATE']).startswith('大于'):
            # 同期线损率TO
            self.inputSel_collecline_loss_rate_to(para['COLLECLINE_LOSS_RATE_TO'])

            # 同期线损率TO值
            self.inputStr_collecline_loss_rate_to_input(para['COLLECLINE_LOSS_RATE_TO_INPUT'])

        # 日期类型
        self.inputChk_date_type(para['DATE_TYPE'])

        # 运算类型
        self.inputChk_compute_type(para['COMPUTE_TYPE'])

        # 台区编号
        self.inputStr_tg_no(para['TG_NO'])

        # 台区名称
        self.inputStr_tg_name(para['TG_NAME'])

        # 查询日期,开始
        self.inputDt_start_date(para['START_DATE'])

        # 查询日期，结束
        self.inputDt_end_date(para['END_DATE'])

        # 责任人工号
        self.inputStr_person_resp_no(para['PERSON_RESP_NO'])

        # 查询按钮
        self.btn_search()

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
    @data(*DataAccess.getCaseData(TgLineLossStatisticsQuery_data.TgLineLossDetail_para))
    def test_query(self, para):
        """高级应用→线损分析→台区线损统计查询→台区线损明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TgLineLossStatisticsQuery_data.TgLineLossDetail_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
