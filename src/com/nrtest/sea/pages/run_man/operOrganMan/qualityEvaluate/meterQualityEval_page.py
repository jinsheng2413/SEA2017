# -*- coding:utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: collTmnlQualityEval_page.py
@time: 2018/11/13 9:20
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→采集运维平台→采集终端质量评价
# 电表质量评价统计
class MeterQualityEvalStaticPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, name):
        # self.click(MeterQualityEvalStaticLocators.CONS_TYPE_SEL)
        # locator = self.get_select_locator(
        #     MeterQualityEvalStaticLocators.CONS_TYPE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 查询日期
    def inputDt_query_date(self, value):
        # self.input(value, *MeterQualityEvalStaticLocators.QUERY_DATE)
        self.inputDate(value)

    # 电表厂家--打开并选择
    def inputSel_meter_fac(self, name):
        # self.click(MeterQualityEvalStaticLocators.METER_FAC_SEL)
        # locator = self.get_select_locator(
        #     MeterQualityEvalStaticLocators.METER_FAC, name)
        # self.click(locator)
        self.selectCheckBox(name, sleep_sec=0.5)

    # 点击查询
    def btn_query(self):
        # self.click(MeterQualityEvalStaticLocators.BTN_QUERY)
        self.btn_query(True)

# 电表质量评价明细
class MeterQualityEvalDetailPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, name):
        # self.click(MeterQualityEvalDetailLocators.CONS_TYPE_SEL)
        # locator = self.get_select_locator(
        #     MeterQualityEvalDetailLocators.CONS_TYPE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 故障严重程度--打开并选择
    def inputSel_fault_level(self, name):
        # self.click(MeterQualityEvalDetailLocators.FAULT_LEVEL_SEL)
        # locator = self.get_select_locator(
        #     MeterQualityEvalDetailLocators.FAULT_LEVEL, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 电表厂家-打开并选择
    def inputRSel_meter_fac(self, name):
        # self.click(MeterQualityEvalDetailLocators.METER_FAC_SEL)
        # locator = self.get_select_locator(
        #     MeterQualityEvalDetailLocators.METER_FAC, name)
        # self.click(locator)
        self.selectCheckBox(name, sleep_sec=0.5)

    # 故障类别-打开并选择
    def inputSel_fault_type(self, name):
        # self.click(MeterQualityEvalDetailLocators.FAULT_TYPE_SEL)
        # locator = self.get_select_locator(
        #     MeterQualityEvalDetailLocators.FAULT_TYPE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 故障开始日期
    def inputDt_query_start_date(self, value):
        # self.input(value, *MeterQualityEvalDetailLocators.START_DATE)
        self.inputDate(value)

    # 故障结束日期
    def inputDt_query_end_date(self, value):
        # self.input(value, *MeterQualityEvalDetailLocators.END_DATE)
        self.inputDate(value)

    # 点击查询
    def btn_query(self):
        # self.click(MeterQualityEvalDetailLocators.BTN_QUERY)
        self.btn_query(True)
