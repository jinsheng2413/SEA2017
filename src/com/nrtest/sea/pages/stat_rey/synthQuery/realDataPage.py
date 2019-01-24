# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→抄表数据查询（冀北）
class RealDataPage(Page):
    # 曲线类型
    def inputChk_curve_type(self, index):
        self.clickRadioBox(index)

    # 曲线类型
    def inputChk_curve_type_failed(self, index):
        self.clickRadioBox(index, is_multi_elements=True, is_multi_tab=True)

    # 终端生产厂家
    def inputSel_Tmnl_manufacturer(self, name):
        # self.click(RealDataLocators.QRY_TMNL_MANUFACTUREE)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_TMNL_MANUFACTUREE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 反相采集结果
    def inputSel_reversCollectionResult(self, name):
        # self.click(RealDataLocators.QRY_REVERS_COLLECT_RESULT)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_REVERS_COLLECT_RESULT_VALUE, name)
        # print(locator)
        # self.click(locator)
        self.selectDropDown(name)

    # 终端运行状态
    def inputSel_TmnlRunState_Failtime(self, name):
        # self.click(RealDataLocators.QRY_TMNL_RUN_STATE_FAILDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_TMNL_RUN_STATE_FAILDETAIL_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name, is_multi_elements=True, is_multi_tab=True)

    # 终端运行状态
    def inputSel_tmnl_run_status_RDetail(self, name):
        # self.click(RealDataLocators.QRY_TMNL_RUN_STATE_RDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_TMNL_RUN_STATE_RDETAIL_VALUE, name)
        # print(locator)
        # self.click(locator)
        self.selectDropDown(name)

    # 电能表抄读状态
    def inputSel_meter_read_status_Rdetail(self, name):
        # self.click(RealDataLocators.QRY_METER_READ_STATE_RDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_METER_READ_STATE_RDETAIL_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 电能表抄读状态
    def inputSel_meter_read_status_faildetail(self, name):
        # self.click(RealDataLocators.QRY_METER_READ_STATE_FAILDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_METER_READ_STATE_FAILDETAIL_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 数据类型
    def inputSel_data_type(self, name):
        # self.click(RealDataLocators.QRY_DATATYPE_RDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_DATATYPE_RDETAIL_VALUE, name)
        # print(locator)
        # self.click(locator)
        self.selectDropDown(name)

    # 相位
    def inputSel_phase_Rdetail(self, name):
        # self.click(RealDataLocators.QRY_PHASE_RDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_PHASE_RDETAIL_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 相位
    def inputSel_phase_Faildetail(self, name):
        # self.click(RealDataLocators.QRY_USER_TYPE_FAILDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_USER_TYPE_FAILDETAIL_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name, is_multi_elements=True, is_multi_tab=True)

    # 抄表段号
    def inputStr_mr_sect_no_Rdetail(self, value):
        self.input(value)  # , *RealDataLocators.QRY_MR_SECT_NO_RDETAIL)

    # 抄表段号
    def inputStr_mr_sect_no_Faildetail(self, value):
        self.input(value)  # , *RealDataLocators.QRY_MR_SECT_NO_FAILDETAIL)

    # 电表资产号
    def inputStr_meter_asset_no_Rdetail(self, value):
        self.input(value)  #, *RealDataLocators.QRY_METER_ASSET_NO_RDETAIL)

    # 电表资产号
    def inputStr_meter_asset_no_Faildetail(self, value):
        self.input(value)  #, *RealDataLocators.QRY_METER_ASSET_NO_FAILDETAIL)

    # 查询时间
    def inputDt_Time_Rdetail(self, value):
        self.inputDate(value)  # , *RealDataLocators.QRY_TIME_RDETAIL)

    # 查询时间
    def inputDt_Time_Faildetail(self, value):
        self.inputDate(value)  #, *RealDataLocators.QRY_TIME_FAILTIME)

    # 用户类型
    def inputSel_cons_type_Rdetail(self, name):
        # self.click(RealDataLocators.QRY_USER_TYPE_RDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_USER_TYPE_RDETAIL_VALUE, name)
        # print(locator)
        # self.click(locator)
        self.selectCheckBox(name)

    # 用户类型
    def inputSel_cons_type_Faildetail(self, name):
        # self.click(RealDataLocators.QRY_USER_TYPE_FAILDETAIL)
        # locator = self.get_select_locator(
        #     RealDataLocators.QRY_USER_TYPE_FAILDETAIL_VALUE, name)
        # self.click(locator)
        self.selectCheckBox(name, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_rdetail_qry(self):
        # self.click(RealDataLocators.BTN_QRY_RDETAIL)
        self.btn_query()

    # 查询
    def btn_Faildetail_qry(self):
        # self.click(RealDataLocators.BTN_QRY_FAILDETAIL)
        self.btn_query(True)