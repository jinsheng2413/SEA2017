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
    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 测量点电流越限统计
class ConsIntrgratedQueryMeasurementPointCurrentOverLimitPage(Page):
    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 测量点不平衡度越限累计时间统计
class ConsIntrgratedQueryMeasurementPointTotalTimePage(Page):
    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 测量点功率因数区段累计时间统计
class ConsIntrgratedQueryMeasurementPointTotalTime2Page(Page):
    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 测量点总及分相有功功率统计
class ConsIntrgratedQueryMeasurementPointTotalActivePowerPage(Page):
    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 测量点直流模拟量越限统计
class ConsIntrgratedQueryMeasurementPointDcSimulationPage(Page):
    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 测量点最大需量及发生时间统计
class ConsIntrgratedQueryMeasurementPointMaxNumAndTimePage(Page):
    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 终端统计数据
class ConsIntrgratedQueryMeasurementPointTmnlStatPage(Page):
    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 总加组统计数据
class ConsIntrgratedQueryMeasurementPointSumGroupStatPage(Page):

    # 总加组
    def inputChk_sum_group(self, value=''):
        self.click(("xpath", '//button[contains(text(),"总加组")]'))

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True)

    # 从
    def inputDt_start_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
