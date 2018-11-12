# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/11/12 9:20
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.operOrganMan.qualityEvaluate.faultDealQualityEval_locators import \
    FaultDealQualityDetailLocators
from com.nrtest.sea.locators.run_man.operOrganMan.qualityEvaluate.faultDealQualityEval_locators import \
    FaultDealQualityStaticLocators
from com.nrtest.sea.locators.run_man.operOrganMan.qualityEvaluate.faultDealQualityEval_locators import \
    StaffDealDetailLocators


# 运行管理→采集运维平台→故障处理质量评价
# 故障处理质量统计
class FaultDealQualityStaticPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*FaultDealQualityStaticLocators.CONS_TYPE_SEL)
        locator = self.get_select_locator(
            FaultDealQualityStaticLocators.CONS_TYPE, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *FaultDealQualityStaticLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*FaultDealQualityStaticLocators.BTN_QUERY)


# 故障处理质量明细
class FaultDealQualityDetailPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*FaultDealQualityDetailLocators.CONS_TYPE_SEL)
        locator = self.get_select_locator(
            FaultDealQualityDetailLocators.CONS_TYPE, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *FaultDealQualityDetailLocators.QUERY_DATE)

    # 流程状态-打开并选择
    def inputRSel_flow_status(self, name):
        self.click(*FaultDealQualityDetailLocators.FLOW_STATUS_SEL)
        locator = self.get_select_locator(
            FaultDealQualityDetailLocators.FLOW_STATUS, name)
        self.click(*locator)

    # 点击查询
    def btn_query(self):
        self.click(*FaultDealQualityDetailLocators.BTN_QUERY)


# 人员处理明细
class StaffDealDetailPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*StaffDealDetailLocators.CONS_TYPE_SEL)
        locator = self.get_select_locator(
            StaffDealDetailLocators.CONS_TYPE, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *StaffDealDetailLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*StaffDealDetailLocators.BTN_QUERY)
