# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_RealData_FailDetail.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.realDataPage import RealDataPage


# 统计查询→综合查询→抄表数据查询（冀北）:抄表失败明细
@ddt
class TestRealData_Faildetail(TestCase, RealDataPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SynthQuery_data.realData_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.realData_fdetail_tab)
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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 曲线类型
        self.inputChk_curve_type_failed(para['CURVE_TYPE_FAILED'])
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 选择抄表段号
        self.inputStr_ReadMeterSegmentNo_Faildetail(
            para['READ_METER_SEGMENT_NO'])
        # 电表资产号
        self.inputStr_MeterAssert_Faildetail(para['METER_ASSERT'])
        # 用户类型
        self.inputSel_userType_Faildetail(para['CONS_TYPE'])
        # 反相采集结果
        self.inputSel_reversCollectionResult(para['REVERS_COLLECTION_RESULT'])
        # 终端生产厂家
        self.inputSel_Tmnl_manufacturer(para['TMNL_MANUFACTURER'])
        # 相位
        self.inputSel_phase_Faildetail(para['PHASE'])
        # 查询日期
        self.inputDt_Time_Faildetail(para['QUERY_TIME'])
        # 电能表抄读状态
        self.inputSel__meter_read_state_faildetail(para['METER_READ_STATE'])
        # 终端运行状态
        self.inputSel_TmnlRunState_Failtime(para['TMNL_RUN_STATE'])
        # 查询
        self.btn_Faildetail_qry()

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
    @data(*DataAccess.getCaseData(SynthQuery_data.realData_para, SynthQuery_data.realData_fdetail_tab))
    def test_query(self, para):
        """统计查询→综合查询→抄表数据查询（冀北）:抄表失败明细

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.realData_para, SynthQuery_data.realData_fdetail_tab, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

