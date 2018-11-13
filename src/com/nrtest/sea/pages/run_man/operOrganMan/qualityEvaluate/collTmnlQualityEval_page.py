# -*- coding:utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: collTmnlQualityEval_page.py
@time: 2018/11/12 15:19
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.operOrganMan.qualityEvaluate.collTmnlQualityEval_locators import \
    TmnlQualityEvalDetailLocators
from com.nrtest.sea.locators.run_man.operOrganMan.qualityEvaluate.collTmnlQualityEval_locators import \
    TmnlQualityEvalStaticLocators


# 运行管理→采集运维平台→采集终端质量评价
# 终端质量评价统计
class TmnlQualityEvalStaticPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*TmnlQualityEvalStaticLocators.CONS_TYPE_SEL)
        locator = self.get_select_locator(
            TmnlQualityEvalStaticLocators.CONS_TYPE, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *TmnlQualityEvalStaticLocators.QUERY_DATE)

    # 终端厂家--打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*TmnlQualityEvalStaticLocators.TMNL_FAC_SEL)
        locator = self.get_select_locator(
            TmnlQualityEvalStaticLocators.TMNL_FAC, name)
        self.click(*locator)

    # 点击查询
    def btn_query(self):
        self.click(*TmnlQualityEvalStaticLocators.BTN_QUERY)


# 终端质量评价明细
class TmnlQualityEvalDetailPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*TmnlQualityEvalDetailLocators.CONS_TYPE_SEL)
        locator = self.get_select_locator(
            TmnlQualityEvalDetailLocators.CONS_TYPE, name)
        self.click(*locator)

    # 故障严重程度--打开并选择
    def inputRSel_fault_level(self, name):
        self.click(*TmnlQualityEvalDetailLocators.FAULT_LEVEL_SEL)
        locator = self.get_select_locator(
            TmnlQualityEvalDetailLocators.FAULT_LEVEL, name)
        self.click(*locator)

    # 终端厂家-打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*TmnlQualityEvalDetailLocators.TMNL_FAC_SEL)
        locator = self.get_select_locator(
            TmnlQualityEvalDetailLocators.TMNL_FAC, name)
        self.click(*locator)

    # 故障类别-打开并选择
    def inputRSel_fault_type(self, name):
        self.click(*TmnlQualityEvalDetailLocators.FAULT_TYPE_SEL)
        locator = self.get_select_locator(
            TmnlQualityEvalDetailLocators.FAULT_TYPE, name)
        self.click(*locator)

    # 故障开始日期
    def inputStr_query_start_date(self, value):
        self.input(value, *TmnlQualityEvalDetailLocators.START_DATE)

    # 故障结束日期
    def inputStr_query_end_date(self, value):
        self.input(value, *TmnlQualityEvalDetailLocators.END_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*TmnlQualityEvalDetailLocators.BTN_QUERY)
