# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_readSuccessNew.py
@time: 2018-09-17 16:30
@desc:
"""

from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.tree.tree_page import TreeQualityPage
from com.nrtest.sea.data.base_app.dataGatherMan.dataGatherMan_data import DataGatherMan_data
from com.nrtest.sea.pages.base_app.dataGatherMan.readSuccessNew_page import GatherSuccessRatePageNew
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→数据采集管理→采集质量检查(new)→采集成功率
@ddt
class TestGatherSuccessRate(TestCase, GatherSuccessRatePageNew):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(DataGatherMan_data.dataGatherQualityAnalyze_new_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(DataGatherMan_data.dataGatherQualityAnalyze_new_readSuccess_tab_readSuccess)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()
        cls.user_page = TreeQualityPage(cls)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新菜单页面
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

        self.user_page.openLeftTree(para['NODE'])
        sleep(2)
        # 选择tab页
        self.inputChk_tab_name(para['TAB_NAME'])
        # 选择小tab页
        self.inputChk_tab_name2(para['TAB_NAME2'])
        tab_name = self.get_para_value(para['TAB_NAME'])
        tab_name2 = self.get_para_value(para['TAB_NAME2'])

        if tab_name == '采集成功率':
            # 打开左边树并选择
            self.openLeftTree(para['TREE_NODE'])
            # 数据类型
            self.inputChk_data_type(para['DATA_TYPE'])
            # 用户类型
            self.inputSel_cons_type(para['CONS_TYPE'])
            # 通信方式
            self.inputSel_comm_mode(para['COMM_MODE'])
            # 终端厂家
            self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
            # 计量方式
            self.inputSel_meas_mode(para['MEAS_MODE'])
            # 所属区域
            self.inputSel_area(para['AREA'])
            # 芯片厂家
            self.inputSel_chip_factory(para['CHIP_FACTORY'])
            # 开始时间
            self.inputDt_start_date(para['START_DATE'])
            # 结束时间
            self.inputDt_end_date(para['END_DATE'])

            if self.get_para_value(para['DATA_TYPE']) in ['功率曲线', '电压曲线', '电流曲线']:
                # 相位
                self.inputSel_phase_code(para['PHASE_CODE'])

            # 点击查询按钮
            self.btn_search()

        elif tab_name == '采集成功率统计':
            # 打开左边树并选择
            self.openLeftTree(para['TREE_NODE'])
            # 数据类型
            self.inputChk_data_type(para['DATA_TYPE'])
            # 用户类型
            self.inputSel_cons_type(para['CONS_TYPE'])
            # 终端厂家
            self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
            # 芯片厂家
            self.inputSel_chip_factory(para['CHIP_FACTORY'])
            # 通讯规约
            self.inputSel_tmnl_protocol(para['TMNL_PROTOCOL'])
            # 查询日期
            self.inputDt_start_date(para['START_DATE'])
            if self.get_para_value(para['DATA_TYPE']) in ['功率曲线', '电压曲线', '电流曲线']:
                # 相位
                self.inputSel_phase_code(para['PHASE_CODE'])
            # 点击查询按钮
            self.btn_search()

        elif tab_name == '采集成功率明细':
            # 打开左边树并选择
            self.openLeftTree(para['TREE_NODE'])
            # 用户类型
            self.inputSel_cons_type(para['CONS_TYPE'])
            # 芯片厂家
            self.inputSel_chip_factory(para['CHIP_FACTORY'])
            # 终端厂家
            self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
            # 通信方式
            self.inputSel_comm_mode(para['COMM_MODE'])
            # 用户编号
            self.inputStr_cons_no(para['CONS_NO'])
            # 终端地址
            self.inputStr_tmnl_addr(para['TMNL_ADDR'])
            # 日期
            self.inputDt_start_date(para['START_DATE'])
            # 点击查询按钮
            self.btn_search()

        elif tab_name == '连续抄表失败明细':
            # 供电单位
            self.openLeftTree(para['TREE_NODE'])

            # 用户类型
            self.inputSel_cons_type(para['CONS_TYPE'])

            if tab_name2 == '连续抄表失败统计':
                # 运行状态
                self.inputSel_run_status(para['RUN_STATUS'])

                # 日期
                self.inputDt_start_date(para['START_DATE'])

            elif tab_name2 == '应采集电表明细':
                # 终端类型
                self.inputSel_tmnl_type(para['TMNL_TYPE'])
                # 计量方式
                self.inputSel_meas_mode(para['MEAS_MODE'])
                # 终端地址
                self.inputStr_tmnl_addr(para['TMNL_ADDR'])
                # 应采集
                self.inputChk_data_collect(para['DATA_COLLECT'])
            elif tab_name2 == '连续N天抄表失败明细':
                # 接线方式
                self.inputSel_wiring_mode(para['WIRING_MODE'])
                # 运行状态
                self.inputSel_run_status(para['RUN_STATUS'])
                # 用户编号
                self.inputStr_cons_no(para['CONS_NO'])
                # 终端地址
                self.inputStr_tmnl_addr(para['TMNL_ADDR'])
                # 连续失败天数
                self.inputStr_read_fail_days(para['READ_FAIL_DAYS'])
                # 查询条件
                self.inputSel_query_condition(para['QUERY_CONDITION'])
                # 终端生产厂家
                self.inputSel_tmnl_scfactory(para['TMNL_ScFACTORY'])
            # 查询
            self.btn_qry()
        if tab_name == '按时间统计':
            # 打开左边树并选择
            self.openLeftTree(para['TREE_NODE'])
            # 数据类型
            self.inputChk_data_type(para['DATA_TYPE'])
            # 查询日期，开始
            self.inputDt_start_date(para['START_DATE'])
            # 查询日期，结束
            self.inputDt_end_date(para['END_DATE'])
            # 用户类型
            self.inputSel_cons_type(para['CONS_TYPE'])
            # 用户范围
            self.inputSel_cons_range(para['CONS_RANGE'])
            # 停电标志
            self.inputSel_power_cut_flag(para['POWER_CUT_FLAG'])
            # 终端类型
            self.inputSel_tmnl_type2(para['TMNL_TYPE2'])
            # 通信方式
            self.inputSel_comm_mode2(para['COMM_MODE2'])
            # 规约类型
            self.inputSel_protocol_type(para['PROTOCOL_TYPE'])
            # 计量方式
            self.inputSel_meas_mode(para['MEAS_MODE'])
            # # 相位
            # self.inputSel_phase_code(para['PHASE_CODE'])
            if self.get_para_value(para['DATA_TYPE']) in ['功率曲线', '电压曲线', '电流曲线']:
                # 相位
                self.inputSel_phase_code(para['PHASE_CODE'])
            # 点击查询按钮
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
    @data(*DataAccess.getCaseData(DataGatherMan_data.dataGatherQualityAnalyze_new_para,
                                  DataGatherMan_data.dataGatherQualityAnalyze_new_readSuccess))
    def test_query(self, para):
        """基本应用→数据采集管理→采集质量检查(new)→采集成功率
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataGatherMan_data.dataGatherQualityAnalyze_new_para,
                                  DataGatherMan_data.dataGatherQualityAnalyze_new_readSuccess))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
