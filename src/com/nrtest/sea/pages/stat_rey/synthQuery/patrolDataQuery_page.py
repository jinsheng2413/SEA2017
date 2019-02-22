# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: patrolDataQuery_page.py
@time: 2018/10/18 14:58
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.patrolDataQuery_locators import PatrolDataQueryLocators


# 统计查询→综合查询→巡检仪数据查询
# 基本档案
class PatrolDataQueryPage(Page):
    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 曲线数据
class PatrolDataQueryCurveDataPage(Page):
    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content, *PatrolDataQueryLocators.CURVE_DATA_CONS_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *PatrolDataQueryLocators.CURVE_DATA_TMNL_ADDR)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 曲线类型
    def inputSel_curve_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 曲线对比
class PatrolDataQueryCurveContrastPage(Page):
    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content, *PatrolDataQueryLocators.CURVE_CONTRAST_TMNL_ASSET_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *PatrolDataQueryLocators.CURVE_CONTRAST_TMNL_ADDR)

    # 曲线类型
    def inputSel_curve_type(self, index):
        self.selectDropDown(index)

    # 电表资产号
    def inputStr_meter_asset_no(self, content):
        self.input(content)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 相别
    def inputChk_phase_code(self, index):
        self.clickRadioBox(index)

    # 参照对象
    def inputChk_reference_object(self, index):
        self.clickRadioBox(index)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)


# 电流回路状态
class PatrolDataQueryCurrentStatusPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *PatrolDataQueryLocators.CURRENT_STATUS_TMNL_ADDR)

    # 电流回路状态
    def inputSel_current_status(self, index):
        self.selectDropDown(index)

    # 相别
    def inputChk_phase_code(self, index):
        self.clickCheckBox_new(index)

    # 日期
    def inputDt_query_date(self, index):
        self.inputDate(index)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content, *PatrolDataQueryLocators.CURRENT_STATUS_TMNL_ASSET_NO)

    # 用户编号
    def inputSel_cons_no(self, content):
        self.input(content, *PatrolDataQueryLocators.CURRENT_STATUS_CONS_NO)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 异常事件查询
class PatrolDataQueryAnomalousEventPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *PatrolDataQueryLocators.ANOMALOUS_EVENT_TMNL_ADDR)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content, *PatrolDataQueryLocators.ANOMALOUS_EVENT_TMNL_ASSET_NO)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content, *PatrolDataQueryLocators.ANOMALOUS_EVENT_CONS_NO)

    # 异常事件
    def inputSel_anomalous_event(self, index):
        self.selectDropDown(index)

    # 事件类型
    def inputChk_event_type(self, index):
        self.clickRadioBox(index)

    # 事件时间
    def inputDt_event_date(self, index):
        self.inputDate(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
