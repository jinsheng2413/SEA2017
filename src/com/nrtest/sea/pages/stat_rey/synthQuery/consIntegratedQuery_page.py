# -*- coding:utf-8 -*-

"""
@author: js
@file:consIntegratedQuery_page.py
@time:2019/2/26 14:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 测量点电压统计
class ConsIntrgratedQueryMeasurementPointVoltagePage(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value)


# 测量点电流越限统计
class ConsIntrgratedQueryMeasurementPointCurrentOverLimitPage(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)


# 测量点不平衡度越限累计时间统计
class ConsIntrgratedQueryMeasurementPointTotalTimePage(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)


# 测量点功率因数区段累计时间统计
class ConsIntrgratedQueryMeasurementPointTotalTime2Page(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)


# 测量点总及分相有功功率统计
class ConsIntrgratedQueryMeasurementPointTotalActivePowerPage(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)


# 测量点直流模拟量越限统计
class ConsIntrgratedQueryMeasurementPointDcSimulationPage(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)


# 测量点最大需量及发生时间统计
class ConsIntrgratedQueryMeasurementPointMaxNumAndTimePage(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)


# 终端统计数据
class ConsIntrgratedQueryMeasurementPointTmnlStatPage(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)


# 总加组统计数据
class ConsIntrgratedQueryMeasurementPointSumGroupStatPage(Page):
    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)
