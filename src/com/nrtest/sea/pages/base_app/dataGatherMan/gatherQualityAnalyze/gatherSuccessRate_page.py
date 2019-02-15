# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: GatherSuccessRatePage.py
@time: 2018-09-17 14:15
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应该→数据采集管理→采集质量分析→采集成功率
# 采集成功率→采集成功率
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_locators import GatherSuccessRateDetailLocators


class GatherSuccessRatePage(Page):
    # 数据类型
    def inputChk_data_type(self, options):
        self.clickRadioBox(options, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_cons_type(self, index):
        # if index == 'c':
        #     self._find_elements(GatherSuccessRateLocators.CONS_TYPE)
        # else:
        #     self.click(GatherSuccessRateLocators.CONS_TYPE)
        #     locator = self.get_select_locator(
        #         GatherSuccessRateLocators.CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(GatherSuccessRateLocators.CONS_TYPE)
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(GatherSuccessRateLocators.TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     GatherSuccessRateLocators.TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 计量方式
    def inputSel_meas_mode(self, index):
        # self.click(GatherSuccessRateLocators.MEAS_MODE)
        # locator = self.get_select_locator(
        #     GatherSuccessRateLocators.MEAS_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 所属区域
    def inputSel_area(self, index):
        # self.click(GatherSuccessRateLocators.AREA)
        # locator = self.get_select_locator(
        #     GatherSuccessRateLocators.AREA_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 芯片厂家
    def inputSel_chip_factory(self, index):
        # self.click(GatherSuccessRateLocators.CHIP_FACTORY)
        # locator = self.get_select_locator(
        #     GatherSuccessRateLocators.CHIP_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询日期开始
    def inputDt_start_date(self, content):
        # self.exec_script(GatherSuccessRateLocators.START_DATE_JS)
        # self.input(content, *GatherSuccessRateLocators.START_DATE)
        self.inputDate(content)

    # 查询日期结束
    def inputDt_end_date(self, content):
        # self.exec_script(GatherSuccessRateLocators.END_DATE_JS)
        # self.input(content, *GatherSuccessRateLocators.END_DATE)
        self.inputDate(content)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        # self.click(GatherSuccessRateLocators.BTN_SEARCH)
        self.btn_query(True)


# 采集成功率→采集成功率统计
class GatherSuccessRateStatPage(Page):
    # 数据类型
    def inputChk_data_type(self, options):
        self.clickRadioBox(options, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_cons_type(self, index):
        # if index == 'c':
        #     self._find_elements(GatherSuccessRateStatLocators.CONS_TYPE)
        # else:
        #     self.click(GatherSuccessRateStatLocators.CONS_TYPE)
        #     locator = self.get_select_locator(
        #         GatherSuccessRateStatLocators.CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(GatherSuccessRateStatLocators.CONS_TYPE)
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(GatherSuccessRateStatLocators.TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     GatherSuccessRateStatLocators.TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 芯片厂家
    def inputSel_chip_factory(self, index):
        # self.click(GatherSuccessRateStatLocators.CHIP_FACTORY)
        # locator = self.get_select_locator(
        #     GatherSuccessRateStatLocators.CHIP_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 通讯规约
    def inputSel_tmnl_protocol(self, index):
        # self.click(GatherSuccessRateStatLocators.TMNL_PROTOCOL)
        # locator = self.get_select_locator(
        #     GatherSuccessRateStatLocators.TMNL_PROTOCOL_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(GatherSuccessRateStatLocators.DATE_JS)
        # self.input(content, *GatherSuccessRateStatLocators.DATE)
        self.inputDate(content)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        # self.click(GatherSuccessRateStatLocators.BTN_SEARCH)
        self.btn_query(True)

# 采集成功率→数据采集成功率明细
class GatherSuccessRateDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, options):
        self.specialSelCheckBox(options, checked_loc=GatherSuccessRateDetailLocators.CONS_TYPE_CHECKED)

    # 芯片厂家
    def inputSel_chip_factory(self, index):
        # self.click(GatherSuccessRateDetailLocators.CHIP_FACTORY)
        # locator = self.get_select_locator(
        #     GatherSuccessRateDetailLocators.CHIP_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(GatherSuccessRateDetailLocators.TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     GatherSuccessRateDetailLocators.TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_comm_mode(self, index):
        # self.click(GatherSuccessRateDetailLocators.COMM_MODE)
        # locator = self.get_select_locator(
        #     GatherSuccessRateDetailLocators.COMM_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)  # , *GatherSuccessRateDetailLocators.CONS_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  # , *GatherSuccessRateDetailLocators.TMNL_ADDR)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(GatherSuccessRateDetailLocators.DATE_JS)
        # self.input(content, *GatherSuccessRateDetailLocators.DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(GatherSuccessRateDetailLocators.BTN_SEARCH)
        self.btn_query(True)

# 采集成功率→连续抄表失败明细
class ContinuousFalseDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        # if index == 'c':
        #     self._find_elements(ContinuousFalseDetailLocators.CONS_TYPE)
        # else:
        #     self.click(ContinuousFalseDetailLocators.CONS_TYPE)
        #     locator = self.get_select_locator(
        #         ContinuousFalseDetailLocators.CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(ContinuousFalseDetailLocators.CONS_TYPE)
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 运行状态
    def inputSel_run_status(self, index):
        # self.click(ContinuousFalseDetailLocators.RUN_STATUS)
        # locator = self.get_select_locator(
        #     ContinuousFalseDetailLocators.RUN_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(ContinuousFalseDetailLocators.DATE_JS)
        # self.input(content, *ContinuousFalseDetailLocators.DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        # self.click(ContinuousFalseDetailLocators.BTN_SEARCH)
        self.btn_query(True)


# 基本应用→数据采集管理→采集质量分析→采集成功率→按时间统计
class GatherSuccessRateTimePage(Page):
    # 数据类型
    def inputChk_data_type(self, options):
        self.clickRadioBox(options, is_multi_tab=True, is_multi_elements=True)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        # self.exec_script(GatherSuccessRateTimeLocators.START_DATE_JS)
        # self.input(content, *GatherSuccessRateTimeLocators.START_DATE)
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        # self.exec_script(GatherSuccessRateTimeLocators.END_DATE_JS)
        # self.input(content, *GatherSuccessRateTimeLocators.END_DATE)
        self.inputDate(content)

    # 用户类型
    def inputSel_cons_type(self, index):
        # if index == 'c':
        #     self._find_elements(GatherSuccessRateTimeLocators.CONS_TYPE)
        # else:
        #     self.click(GatherSuccessRateTimeLocators.CONS_TYPE)
        #     locator = self.get_select_locator(
        #         GatherSuccessRateTimeLocators.CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(GatherSuccessRateTimeLocators.CONS_TYPE)
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 用户范围
    def inputSel_cons_range(self, index):
        # self.click(GatherSuccessRateTimeLocators.CONS_RANGE)
        # locator = self.get_select_locator(
        #     GatherSuccessRateTimeLocators.CONS_RANGE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 停电标志
    def inputSel_power_cut_flag(self, index):
        # self.click(GatherSuccessRateTimeLocators.POWER_CUT_FLAG)
        # locator = self.get_select_locator(
        #     GatherSuccessRateTimeLocators.POWER_CUT_FLAG_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        # if index == 'c':
        #     self._find_elements(GatherSuccessRateTimeLocators.TMNL_TYPE)
        # else:
        #     self.click(GatherSuccessRateTimeLocators.TMNL_TYPE)
        #     locator = self.get_select_locator(
        #         GatherSuccessRateTimeLocators.TMNL_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(GatherSuccessRateTimeLocators.TMNL_TYPE)
        self.selectCheckBox(index, is_multi_tab=False, is_multi_elements=False)

    # 规约类型
    def inputSel_protocol_type(self, index):
        # if index == 'c':
        #     self._find_elements(GatherSuccessRateTimeLocators.PROTOCOL_TYPE)
        # else:
        #     self.click(GatherSuccessRateTimeLocators.PROTOCOL_TYPE)
        #     locator = self.get_select_locator(
        #         GatherSuccessRateTimeLocators.PROTOCOL_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(GatherSuccessRateTimeLocators.PROTOCOL_TYPE)
        self.selectCheckBox(index, is_multi_tab=False, is_multi_elements=False)

    # 计量方式
    def inputSel_meas_mode(self, index):
        # self.click(GatherSuccessRateTimeLocators.MEAS_MODE)
        # locator = self.get_select_locator(
        #     GatherSuccessRateTimeLocators.MEAS_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        # self.click(GatherSuccessRateTimeLocators.BTN_SEARCH)
        self.btn_query(True)
