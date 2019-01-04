# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: patrolDataQuery_page.py
@time: 2018/10/18 14:58
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→巡检仪数据查询
class PatrolDataQueryPage(Page):
    # 基本档案
    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content)  # , *PatrolDataQueryLocators.TMNL_ASSET_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.TMNL_ADDR)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CONS_NO)

    # 查询按钮
    def btn_search(self):
        # self.click(PatrolDataQueryLocators.BTN_SEARCH)
        self.btn_query()

    # 曲线数据
    # 用户编号
    def inputStr_curve_data_cons_no(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CURVE_DATA_CONS_NO)

    # 终端地址
    def inputStr_curve_data_tmnl_addr(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CURVE_DATA_TMNL_ADDR)

    # 日期
    def inputStr_curve_data_date(self, content):
        # self.exec_script(PatrolDataQueryLocators.CURVE_DATA_DATE_JS)
        # self.input(content, *PatrolDataQueryLocators.CURVE_DATA_DATE)
        self.inputDate(content)

    # 曲线类型
    def inputSel_curve_data_curve_type(self, index):
        # self.click(PatrolDataQueryLocators.CURVE_DATA_CURVE_TYPE)
        # locator = self.get_select_locator(
        #     PatrolDataQueryLocators.CURVE_DATA_CURVE_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_curve_data_search(self):
        # self.click(PatrolDataQueryLocators.BTN_CURVE_DATA_SEARCH)
        self.btn_query(True)

    # 曲线对比
    # 终端资产号
    def inputStr_curve_contrast_tmnl_asset_no(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CURVE_CONTRAST_TMNL_ASSET_NO)

    # 终端地址
    def inputStr_curve_contrast_tmnl_addr(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CURVE_CONTRAST_TMNL_ADDR)

    # 曲线类型
    def inputSel_curve_contrast_curve_type(self, index):
        # self.click(PatrolDataQueryLocators.CURVE_CONTRAST_CURVE_TYPE)
        # locator = self.get_select_locator(
        #     PatrolDataQueryLocators.CURVE_CONTRAST_CURVE_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 电表资产号
    def inputStr_curve_contrast_meter_asset_no(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CURVE_CONTRAST_METER_ASSET_NO)

    # 日期
    def inputDt_curve_contrast_date(self, content):
        # self.exec_script(PatrolDataQueryLocators.CURVE_CONTRAST_DATE_JS)
        # self.input(content, *PatrolDataQueryLocators.CURVE_CONTRAST_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_curve_contrast_search(self):
        # self.click(PatrolDataQueryLocators.BTN_CONTRAST_DATA_SEARCH)
        self.btn_query(True)

    # 电流回路状态
    # 终端地址
    def inputStr_current_status_tmnl_addr(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CURRENT_STATUS_TMNL_ADDR)

    # 电流回路状态
    def inputSel_current_status(self, index):
        # self.click(PatrolDataQueryLocators.CURRENT_STATUS)
        # locator = self.get_select_locator(
        #     PatrolDataQueryLocators.CURRENT_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 日期
    def inputDt_current_status_date(self, index):
        # self.exec_script(PatrolDataQueryLocators.CURRENT_STATUS_DATE_JS)
        # self.input(index, *PatrolDataQueryLocators.CURRENT_STATUS_DATE)
        self.inputDate(index)

    # 终端资产号
    def inputStr_current_status_tmnl_asset_no(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CURRENT_STATUS_TMNL_ASSET_NO)

    # 用户编号
    def inputSel_current_status_cons_no(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.CURRENT_STATUS_CONS_NO)

    # 查询按钮
    def btn_current_status_search(self):
        # self.click(PatrolDataQueryLocators.BTN_CURRENT_STATUS_SEARCH)
        self.btn_query(True)

    # 异常事件查询
    # 终端地址
    def inputStr_anomalous_event_tmnl_addr(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.ANOMALOUS_EVENT_TMNL_ADDR)

    # 终端资产号
    def inputStr_anomalous_event_tmnl_asset_no(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.ANOMALOUS_EVENT_TMNL_ASSET_NO)

    # 用户编号
    def inputStr_anomalous_event_cons_no(self, content):
        self.input(content)  #, *PatrolDataQueryLocators.ANOMALOUS_EVENT_CONS_NO)

    # 异常事件
    def inputSel_anomalous_event(self, index):
        # self.click(PatrolDataQueryLocators.ANOMALOUS_EVENT)
        # locator = self.get_select_locator(
        #     PatrolDataQueryLocators.ANOMALOUS_EVENT_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_anomalous_event_search(self):
        # self.click(PatrolDataQueryLocators.BTN_ANOMALOUS_EVENT_SEARCH)
        self.btn_query(True)
