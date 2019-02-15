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
from com.nrtest.sea.pages.stat_rey.synthQuery.meterDataQuery_page import MeterDataQueryDetailPage


# 统计查询→综合查询→抄表数据查询:抄表明细
@ddt
class test_MeterDataQueryDetail(TestCase, MeterDataQueryDetailPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SynthQuery_data.MeterDataQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.MeterDataQuery_detail_tab)
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

        # 节点名
        self.openLeftTree(para['TREE_NODE'])

        # 日冻结曲线类型
        self.inputChk_day_freeze_curve_type(para['DAY_FREEZE_CURVE_TYPE'])
        val = self.get_para_value(para['DAY_FREEZE_CURVE_TYPE'])
        is_uip_curve = val in ['日冻结电压曲线', '日冻结电流曲线', '日冻结功率曲线']
        if is_uip_curve:
            # 相位
            self.inputSel_phase_code(para['PHASE_CODE'])

        # 抄表段号
        self.inputStr_mr_sect_no(para['MR_SECT_NO'])

        # 电表资产号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])

        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])

        # 数据类别
        self.inputSel_data_sort(para['DATA_SORT'])

        # 电能表抄读状态
        self.inputSel_meter_read_status(para['METER_READ_STATUS'])

        # 终端运行状态
        self.inputSel_tmnl_run_status(para['TMNL_RUN_STATUS'])

        # 用户类别
        self.inputSel_cons_sort(para['CONS_SORT'])

        # 查询日期
        self.inputDt_query_date(para['QUERY_DATE'])

        # 农排用户选择
        self.inputSel_user_select(para['USER_SELECT'])

        if val == '日冻结电能示值':
            # 采集情况
            self.inputChk_read_status(para['READ_STATUS'])

        # 查询
        self.btn_qry()

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
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterDataQuery_para, SynthQuery_data.MeterDataQuery_detail_tab))
    def test_query(self, para):
        """统计查询→综合查询→抄表数据查询:抄表失败明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterDataQuery_para, SynthQuery_data.MeterDataQuery_detail_tab,
                                  valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
