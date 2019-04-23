# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: gatherSuccessRate_page.py
@time: 2018-09-17 14:15
@desc:
"""

from com.nrtest.common.base_page import Page

# 基本应该→数据采集管理→采集质量分析→采集成功率
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_locators import \
    GatherSuccessRateDetailLocators


# 采集成功率→采集成功率
class GatherSuccessRatePage(Page):
    # 数据类型
    def inputChk_data_type(self, options):
        self.clickRadioBox(options, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options, is_multi_tab=True, is_multi_elements=True, unchecked_cls=True)
        # self.specialSelCheckBox(options, checked_loc=GatherSuccessRateDetailLocators.SEL_CHECKED)

    # 通信方式
    def inputSel_comm_mode(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 计量方式
    def inputSel_meas_mode(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 所属区域
    def inputSel_area(self, index):
        self.selectDropDown(index)

    # 芯片厂家
    def inputSel_chip_factory(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询日期开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 采集成功率→采集成功率统计
class GatherSuccessRateStatPage(Page):
    # 数据类型
    def inputChk_data_type(self, options):
        self.clickRadioBox(options, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options, is_multi_tab=True, is_multi_elements=True, unchecked_cls=True)
        # self.specialSelCheckBox(options, checked_loc=GatherSuccessRateDetailLocators.SEL_CHECKED)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 芯片厂家
    def inputSel_chip_factory(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 通讯规约
    def inputSel_tmnl_protocol(self, index):
        self.selectDropDown(index)

    # 通信方式
    def inputSel_comm_mode(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)


# 采集成功率→采集成功率明细
class GatherSuccessRateDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, options):
        self.specialSelCheckBox(options, checked_loc=GatherSuccessRateDetailLocators.SEL_CHECKED)

    # 芯片厂家
    def inputSel_chip_factory(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_comm_mode(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 采集成功率→连续抄表失败明细
class ContinuousFalseDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options, is_multi_tab=True, is_multi_elements=True, unchecked_cls=True)
        # self.specialSelCheckBox(options, checked_loc=GatherSuccessRateDetailLocators.SEL_CHECKED)

    # 运行状态
    def inputSel_run_status(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # Tab项名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 接线方式
    def inputSel_wiring_mode(self, option):
        self.clean_label(option)
        self.selectDropDown(option)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 连续失败天数
    def inputStr_read_fail_days(self, value):
        self.input(value)

    # 查询条件
    def inputSel_query_condition(self, option):
        self.selectDropDown(option)

    # 终端生产厂家
    def inputSel_tmnl_factory(self, option):
        self.selectDropDown(option)

    # 终端类型
    def inputSel_tmnl_type(self, options):
        self.clean_label(options)
        self.selectDropDown(options)

    # 计量方式
    def inputSel_meas_mode(self, option):
        self.clean_label(option)
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 应采集
    def inputChk_data_collect(self, item):
        self.clickSingleCheckBox(item)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→数据采集管理→采集质量分析→采集成功率:按时间统计
class GatherSuccessRateTimePage(Page):
    # 数据类型
    def inputChk_data_type(self, options):
        self.clickRadioBox(options, is_multi_tab=True, is_multi_elements=True)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options, is_multi_tab=True, is_multi_elements=True, unchecked_cls=True)

    # 用户范围
    def inputSel_cons_range(self, index):
        self.selectDropDown(index)

    # 停电标志
    def inputSel_power_cut_flag(self, index):
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, options):
        self.selectCheckBox(options, unchecked_cls=True)

    # 通信方式
    def inputSel_comm_mode(self, option):
        self.selectCheckBox(option, is_multi_tab=True, is_multi_elements=False)

    # 规约类型
    def inputSel_protocol_type(self, options):
        self.selectCheckBox(options, unchecked_cls=True)

    # 计量方式
    def inputSel_meas_mode(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
