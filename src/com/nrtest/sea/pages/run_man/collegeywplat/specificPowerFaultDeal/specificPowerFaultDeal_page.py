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


# 运行管理-->采集运维平台-->采集故障处理
# 我的待办专变
class FaultSpecificPowerMyTodoPage(Page):
    # 故障严重程度
    def inputChk_job_method(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 故障处理专变

class FaultSpecificPowerDealPage(Page):
    # 故障严重程度
    def inputSel_fault_severity(self, options):
        self.selectDropDown(options)

    # 故障来源
    def inputDt_fault_from(self, options):
        self.selectDropDown(options)

    # 故障开始日期
    def inputDt_fault_start_date(self, value):
        self.inputDate(value)

    # 流程状态
    def inputSel_process(self, options):
        self.selectDropDown(options)

    # 故障结束日期
    def inputDt_fault_end_date(self, value):
        self.inputDate(value)

    # 故障类型
    def inputChk_fault_type(self, items):
        self.clickCheckBox(items, FaultHandlerLocators.QRY_FAULT_TYPE, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 故障反馈专变
class FaultSpecificPowerFeedbackPage(Page):

    # 故障严重程度
    def inputSel_fault_severity(self, options):
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 故障来源
    def inputDt_fault_from(self, options):
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 故障开始日期
    def inputDt_fault_start_date(self, value):
        self.inputDate(value)

    # 流程状态
    def inputSel_process(self, options):
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 故障结束日期
    def inputDt_fault_end_date(self, value):
        self.inputDate(value)

    # 故障类型
    def inputChk_fault_type(self, items):
        self.clickCheckBox(items, FaultFeedBackLocators.QRY_FAULT_TYPE, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
