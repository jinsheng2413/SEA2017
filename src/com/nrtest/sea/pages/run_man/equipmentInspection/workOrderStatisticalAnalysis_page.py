# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: work_order_statistical_analysis_page.py
@time: 2019-02-14 10:25:42
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→设备巡检→工单统计分析:工单统计
class WorkOrderStatisticalAnalysis_count_Page(Page):
    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 参数指标项
    def inputSel_para_tpi_nape(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 包含仪器
    def inputChk_instrument(self, option):
        self.clickRadioBox(option, is_multi_tab=True, is_multi_elements=True)

    # 日月
    def inputChk_day_month(self, option):
        self.clickRadioBox(option, is_multi_elements=True, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 运行管理→设备巡检→工单统计分析:工单明细查询
class WorkOrderStatisticalAnalysis_query_Page(Page):
    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 参数指标项
    def inputSel_para_tpi_nape(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 包含仪器
    def inputChk_instrument(self, option):
        self.clickRadioBox(option, is_multi_tab=True, is_multi_elements=True)

    # 日月
    def inputChk_day_month(self, option):
        self.clickRadioBox(option)

    # 厂家
    def inputSel_manufactory(self, option):
        self.selectDropDown(option)

    # 工单状态
    def inputSel_work_order_status(self, option):
        self.selectDropDown(option, is_equalText=True)

    # 工单编号
    def inputStr_work_order_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
