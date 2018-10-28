# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.realData_locators import RealDataLocators


# 统计查询→综合查询→抄表数据查询（冀北）
class RealDataPage(Page):
    # 终端生产厂家
    def inputSel_Tmnl_manufacturer(self, name):
        self.click(*RealDataLocators.QRY_TMNL_MANUFACTUREE)
        locator = self.get_select_locator(RealDataLocators.QRY_TMNL_MANUFACTUREE_VALUE, name)
        self.click(*locator)

    # 反相采集结果
    def inputSel_reversCollectionResult(self, name):
        self.click(*RealDataLocators.QRY_REVERS_COLLECT_RESULT)
        locator = self.get_select_locator(RealDataLocators.QRY_REVERS_COLLECT_RESULT_VALUE, name)
        print(locator)
        self.click(*locator)

    # 终端运行状态
    def inputSel_TmnlRunState_Failtime(self, name):
        self.click(*RealDataLocators.QRY_TMNL_RUN_STATE_FAILDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_TMNL_RUN_STATE_FAILDETAIL_VALUE, name)
        self.click(*locator)

    # 终端运行状态
    def inputSel_TmnlRunState_RDetail(self, name):
        self.click(*RealDataLocators.QRY_TMNL_RUN_STATE_RDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_TMNL_RUN_STATE_RDETAIL_VALUE, name)
        print(locator)
        self.click(*locator)

    # 电能表抄读状态
    def inputSel_meter_read_state_Rdetail(self, name):
        self.click(*RealDataLocators.QRY_METER_READ_STATE_RDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_METER_READ_STATE_RDETAIL_VALUE, name)
        self.click(*locator)

    # 电能表抄读状态
    def inputSel__meter_read_state_faildetail(self, name):
        self.click(*RealDataLocators.QRY_METER_READ_STATE_FAILDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_METER_READ_STATE_FAILDETAIL_VALUE, name)
        self.click(*locator)

    # 数据类型
    def inputSel_dataType(self, name):
        self.click(*RealDataLocators.QRY_DATATYPE_RDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_DATATYPE_RDETAIL_VALUE, name)
        print(locator)
        self.click(*locator)

    # 相位
    def inputSel_phase_Rdetail(self, name):
        self.click(*RealDataLocators.QRY_PHASE_RDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_PHASE_RDETAIL_VALUE, name)
        self.click(*locator)

    # 相位
    def inputSel_phase_Faildetail(self, name):
        self.click(*RealDataLocators.QRY_USER_TYPE_FAILDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_USER_TYPE_FAILDETAIL_VALUE, name)
        self.click(*locator)

    # 抄表段号
    def inputStr_ReadMeterSegmentNo_Rdetail(self, value):
        self.input(value, *RealDataLocators.QRY_READ_METER_SEGMENT_NO_RDETAIL)

    # 抄表段号
    def inputStr_ReadMeterSegmentNo_Faildetail(self, value):
        self.input(value, *RealDataLocators.QRY_READ_METER_SEGMENT_NO_FAILDETAIL)

    # 电表资产号
    def inputStr_MeterAssert_Rdetail(self, value):
        self.input(value, *RealDataLocators.QRY_METER_ASSET_NO_RDETAIL)

    # 电表资产号
    def inputStr_MeterAssert_Faildetail(self, value):
        self.input(value, *RealDataLocators.QRY_METER_ASSET_NO_FAILDETAIL)

    # 查询时间
    def inputStr_Time_Rdetail(self, value):
        self.input(value, *RealDataLocators.QRY_TIME_RDETAIL)

    # 查询时间
    def inputStr_Time_Faildetail(self, value):
        self.input(value, *RealDataLocators.QRY_TIME_FAILTIME)

    # 用户类型
    def inputSel_userType_Rdetail(self, name):
        self.click(*RealDataLocators.QRY_USER_TYPE_RDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_USER_TYPE_RDETAIL_VALUE, name)
        print(locator)
        self.click(*locator)

    # 用户类型
    def inputSel_userType_Faildetail(self, name):
        self.click(*RealDataLocators.QRY_USER_TYPE_FAILDETAIL)
        locator = self.get_select_locator(RealDataLocators.QRY_USER_TYPE_FAILDETAIL_VALUE, name)
        self.click(*locator)

    # 查询
    def btn_rdetail_qry(self):
        self.click(*RealDataLocators.BTN_QRY_RDETAIL)

        # 查询

    def btn_Faildetail_qry(self):
        self.click(*RealDataLocators.BTN_QRY_FAILDETAIL)
