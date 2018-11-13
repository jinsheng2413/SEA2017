# -*- coding:utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: collTmnlQualityEval_page.py
@time: 2018/11/13 9:20
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.operOrganMan.qualityEvaluate.meterQualityEval_locators import \
    MeterQualityEvalDetailLocators
from com.nrtest.sea.locators.run_man.operOrganMan.qualityEvaluate.meterQualityEval_locators import \
    MeterQualityEvalStaticLocators


# 运行管理→采集运维平台→采集终端质量评价
# 电表质量评价统计
class MeterQualityEvalStaticPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*MeterQualityEvalStaticLocators.CONS_TYPE_SEL)
        locator = self.get_select_locator(
            MeterQualityEvalStaticLocators.CONS_TYPE, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *MeterQualityEvalStaticLocators.QUERY_DATE)

    # 电表厂家--打开并选择
    def inputRSel_meter_fac(self, name):
        self.click(*MeterQualityEvalStaticLocators.METER_FAC_SEL)
        locator = self.get_select_locator(
            MeterQualityEvalStaticLocators.METER_FAC, name)
        self.click(*locator)

    # 点击查询
    def btn_query(self):
        self.click(*MeterQualityEvalStaticLocators.BTN_QUERY)


# 电表质量评价明细
class MeterQualityEvalDetailPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*MeterQualityEvalDetailLocators.CONS_TYPE_SEL)
        locator = self.get_select_locator(
            MeterQualityEvalDetailLocators.CONS_TYPE, name)
        self.click(*locator)

    # 故障严重程度--打开并选择
    def inputRSel_fault_level(self, name):
        self.click(*MeterQualityEvalDetailLocators.FAULT_LEVEL_SEL)
        locator = self.get_select_locator(
            MeterQualityEvalDetailLocators.FAULT_LEVEL, name)
        self.click(*locator)

    # 电表厂家-打开并选择
    def inputRSel_meter_fac(self, name):
        self.click(*MeterQualityEvalDetailLocators.METER_FAC_SEL)
        locator = self.get_select_locator(
            MeterQualityEvalDetailLocators.METER_FAC, name)
        self.click(*locator)

    # 故障类别-打开并选择
    def inputRSel_fault_type(self, name):
        self.click(*MeterQualityEvalDetailLocators.FAULT_TYPE_SEL)
        locator = self.get_select_locator(
            MeterQualityEvalDetailLocators.FAULT_TYPE, name)
        self.click(*locator)

    # 故障开始日期
    def inputStr_query_start_date(self, value):
        self.input(value, *MeterQualityEvalDetailLocators.START_DATE)

    # 故障结束日期
    def inputStr_query_end_date(self, value):
        self.input(value, *MeterQualityEvalDetailLocators.END_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*MeterQualityEvalDetailLocators.BTN_QUERY)
