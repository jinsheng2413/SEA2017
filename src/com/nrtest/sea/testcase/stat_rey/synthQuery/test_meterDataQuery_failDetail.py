# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_meterDataQuery_failDetail.py
@time: 2019-02-12 15:59:56
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
# 统计查询→综合查询→抄表数据查询:抄表失败明细
from com.nrtest.sea.pages.stat_rey.synthQuery.meterDataQuery_page import MeterDataQueryFailDetailPage


# 统计查询→综合查询→抄表数据查询:抄表失败明细
@ddt
class TestMeterDataQueryFailDetail(TestCase, MeterDataQueryFailDetailPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SynthQuery_data.MeterDataQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.MeterDataQuery_fialDetail_tab)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 关闭菜单页面
        cls.closePages(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        每个测试用例测试结束后的操作，在这里做相关清理工作
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
        l = 0
        # 节点名
        self.openLeftTree(para['TREE_NODE'])
        # 日冻结电能市值
        day_ele_value = self.get_para_value(para['DAY_FREEZING_ELE_VALUE'])
        if day_ele_value == '日冻结电能示值':
            l = 1
            self.inputChk_day_freezing_ele_value(para['DAY_FREEZING_ELE_VALUE'])
        # 日冻结需量和市值曲线
        day_fdv_curve = self.get_para_value(para['DAY_FREEZING_DEMAND_VALUE_CURVE'])
        if day_fdv_curve in ['日冻结需量', '市值曲线']:
            l = 2
            self.inputChk_day_freezing_demand_value_curve(para['DAY_FREEZING_DEMAND_VALUE_CURVE'])
        # 日冻结曲线类型
        day_curve_type = self.get_para_value(para['DAY_FREEZE_CURVE_TYPE'])
        if day_curve_type in ['日冻结电压曲线', '日冻结电流曲线', '日冻结功率曲线']:
            l = 3
            self.inputChk_day_freeze_curve_type(para['DAY_FREEZE_CURVE_TYPE'])
        # 相位
        self.inputSel_phase_code(para['PHASE_CODE'], line=l)

        # 正反是否有功
        self.inputChk_power_type(para['POWER_TYPE'], line=l)
        # 反相采集结果
        self.inputSel_recerse_collection_result(para['RECERSE_COLLECTION_RESULT'], line=l)

        # 抄表段号
        self.inputStr_mr_sect_no(para['MR_SECT_NO'])
        # 电表资产号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 终端厂家
        self.inputSel_tmnl_manufacturer(para['TMNL_MANUFACTURER'])
        # 计量点状态
        self.inputSel_sto_point_status(para['STO_POINT_STATUS'])
        # 规约类型
        self.inputChk_protocol_type(para['PROTOCOL_TYPE'])
        # 查询日期
        self.inputDt_query_date(para['QUERY_DATE'])
        # 农排用户选择
        self.inputSel_user_select(para['USER_SELECT'])
        # 查询
        self.btn_qry()
        print('------------')

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
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterDataQuery_para, SynthQuery_data.MeterDataQuery_fialDetail_tab))
    def test_query(self, para):
        """统计查询→综合查询→抄表数据查询:抄表失败明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterDataQuery_para, SynthQuery_data.MeterDataQuery_fialDetail_tab,
                                  valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
