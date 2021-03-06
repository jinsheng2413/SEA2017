# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_MeterQualityEvalDetail.py
@time: 2018/11/13 9:20
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.operOrganMan.operOrganMan_data import OperOrganManData
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.collegeywplat.qualityEvaluate.meterQualityEval_page import \
    MeterQualityEvalDetailPage


# 运行管理→采集运维平台→电能表质量评价:电表质量评价明细
@ddt
class TestMeterQualityEvalDetail(TestCase, MeterQualityEvalDetailPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(OperOrganManData.para_MeterQualityEval)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(OperOrganManData.para_MeterQualityEvalDetail)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭页面
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
        """
        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 供电单位
        self.openLeftTree(para['TREE_NODE'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 故障严重程度
        self.inputSel_fault_severity(para['FAULT_SEVERITY'])
        # 电表厂家
        self.inputSel_meter_factory(para['METER_FACTORY'])
        # 故障类别
        self.inputSel_fault_type(para['FAULT_TYPE'])
        # 故障开始日期
        self.inputDt_start_date(para['START_DATE'])
        # 故障开始日期
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
        self.assertTrue(self.check_query_criteria(para))

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(OperOrganManData.para_MeterQualityEval, OperOrganManData.para_MeterQualityEvalDetail))
    def test_query(self, para):
        """运行管理→采集运维平台→采集终端质量评价:电表质量评价明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(OperOrganManData.para_MeterQualityEval, OperOrganManData.para_MeterQualityEvalDetail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
