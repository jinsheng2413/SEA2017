# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: faultHandler_page.py
@time: 2018/11/12 0012 9:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.collegeywplat.acquistionFaultHandling.faultHandler_locators import \
    FaultHandlerLocators,FaultFeedBackLocators


#运行管理-->采集运维平台-->采集故障处理-->专变故障处理
class FaultSpecificPowerDealPage(Page):
    # 故障严重程度
    def inputSel_faultSeverity(self, options):
        # self.click(*FaultHandlerLocators.QRY_FAULT_SEVERITY)
        # locator = self.get_select_locator(FaultHandlerLocators.QRY_FAULT_SEVERITY_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options)

    # 故障来源
    def inputSel_faultFrom(self, options):
        # self.click(*FaultHandlerLocators.QRY_FAULT_FROM)
        # locator = self.get_select_locator(FaultHandlerLocators.QRY_FAULT_FROM_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options)

    # 故障开始日期
    def inputStr_faultStartDate(self, value):
        # self.input(value, *FaultHandlerLocators.QRY_FAULT_START_DATE)
        self.inputDate(value)

    # 流程状态
    def inputSel_process(self, options):
        # self.click(*FaultHandlerLocators.QRY_PROCESS_STAUS)
        # locator = self.get_select_locator(FaultHandlerLocators.QRY_PROCESS_STAUS_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options)

    # 故障结束日期
    def inputStr_faultEndDate(self, value):
        # self.input(value, *FaultHandlerLocators.QRY_FAULT_END_DATE)
        self.inputDate(value)

    # 故障类型
    def inputChk_fault_type(self, items):
        self.clickCheckBox(items, FaultHandlerLocators.QRY_FAULT_TYPE, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        # self.click(*FaultHandlerLocators.BTN_QRY)
        self.btn_query(True)


class FaultSpecificPowerFeedbackPage(Page):
    # 故障严重程度
    def inputSel_faultSeverity(self, options):
        # self.click(*FaultFeedBackLocators.QRY_FAULT_SEVERITY)
        # locator = self.get_select_locator(FaultFeedBackLocators.QRY_FAULT_SEVERITY_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 故障来源
    def inputSel_faultFrom(self, options):
        # self.click(*FaultFeedBackLocators.QRY_FAULT_FROM)
        # locator = self.get_select_locator(FaultFeedBackLocators.QRY_FAULT_FROM_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 故障开始日期
    def inputStr_faultStartDate(self, value):
        # self.input(value, *FaultFeedBackLocators.QRY_FAULT_START_DATE)
        self.inputDate(value)

    # 流程状态
    def inputSel_process(self, options):
        # self.click(*FaultFeedBackLocators.QRY_PROCESS_STAUS)
        # locator = self.get_select_locator(FaultFeedBackLocators.QRY_PROCESS_STAUS_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options,is_multi_tab=True, is_multi_elements=True)

    # 故障结束日期
    def inputStr_faultEndDate(self, value):
        # self.input(value, *FaultFeedBackLocators.QRY_FAULT_END_DATE)
        self.inputDate(value)

    # 故障类型
    def inputChk_fault_type(self, items):
        self.clickCheckBox(items, FaultFeedBackLocators.QRY_FAULT_TYPE, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        # self.click(*FaultFeedBackLocators.BTN_QRY)
        self.btn_query(True)

