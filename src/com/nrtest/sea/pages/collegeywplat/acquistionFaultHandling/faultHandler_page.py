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
class FaultHandlerPage(Page):
    # 故障严重程度
    def inputSel_faultSeverity(self, name):
        self.click(*FaultHandlerLocators.QRY_FAULT_SEVERITY)
        locator = self.get_select_locator(FaultHandlerLocators.QRY_FAULT_SEVERITY_VALUE, name)
        self.click(*locator)

    # 故障来源
    def inputSel_faultFrom(self, name):
        self.click(*FaultHandlerLocators.QRY_FAULT_FROM)
        locator = self.get_select_locator(FaultHandlerLocators.QRY_FAULT_FROM_VALUE, name)
        self.click(*locator)

    # 故障开始日期
    def inputStr_faultStartDate(self, value):
        self.input(value, *FaultHandlerLocators.QRY_FAULT_START_DATE)

    # 流程状态
    def inputSel_process(self, name):
        self.click(*FaultHandlerLocators.QRY_PROCESS_STAUS)
        locator = self.get_select_locator(FaultHandlerLocators.QRY_PROCESS_STAUS_VALUE, name)
        self.click(*locator)

    # 故障结束日期
    def inputStr_faultEndDate(self, value):
        self.input(value, *FaultHandlerLocators.QRY_FAULT_END_DATE)


        # 查询
    def btn_qry(self):
            self.click(*FaultHandlerLocators.BTN_QRY)


class FaultFeedBackPage(Page):
    # 故障严重程度
    def inputSel_faultSeverity(self, name):
        self.click(*FaultFeedBackLocators.QRY_FAULT_SEVERITY)
        locator = self.get_select_locator(FaultFeedBackLocators.QRY_FAULT_SEVERITY_VALUE, name)
        self.click(*locator)

    # 故障来源
    def inputSel_faultFrom(self, name):
        self.click(*FaultFeedBackLocators.QRY_FAULT_FROM)
        locator = self.get_select_locator(FaultFeedBackLocators.QRY_FAULT_FROM_VALUE, name)
        self.click(*locator)

    # 故障开始日期
    def inputStr_faultStartDate(self, value):
        self.input(value, *FaultFeedBackLocators.QRY_FAULT_START_DATE)

    # 流程状态
    def inputSel_process(self, name):
        self.click(*FaultFeedBackLocators.QRY_PROCESS_STAUS)
        locator = self.get_select_locator(FaultFeedBackLocators.QRY_PROCESS_STAUS_VALUE, name)
        self.click(*locator)

    # 故障结束日期
    def inputStr_faultEndDate(self, value):
        self.input(value, *FaultFeedBackLocators.QRY_FAULT_END_DATE)

        # 查询

    def btn_qry(self):
        self.click(*FaultFeedBackLocators.BTN_QRY)

