# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossAnalysis_page.py
@time: 2018/10/30 16:21
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→线损统计分析→线路线损分析
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossAnalysis_locators import LineLossAnalysisLocators


class LineLossAnalysisPage(Page):
    # 线损率
    def inputSel_line_loss_rate(self, option):
        self.clean_label(option)
        self.selectDropDown(option)

    # 线损率值
    def inputStr_line_loss_rate_input(self, value):
        self.specialInput(LineLossAnalysisLocators.QRY_INPUT, value, 1)

    # 线损率TO
    def inputSel_line_loss_rate_to(self, option):
        self.specialDropdown(option, LineLossAnalysisLocators.QRY_SEL)

    # 线损率TO值
    def inputStr_line_loss_rate_to_input(self, value):
        self.specialInput(LineLossAnalysisLocators.QRY_INPUT, value, 2)

    # 线路编号
    def inputStr_line_no(self, value):
        self.input(value)

    # 线路名称
    def inputStr_line_name(self, value):
        self.input(value)

    # 线损类型
    def inputChk_loss_line_type(self, option):
        self.clickRadioBox(option)

    # 按日期类型
    def inputChk_qry_date_type(self, option):
        self.clickRadioBox(option)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 从
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 到
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 季度
    def inputChk_quarter(self, option):
        self.clickRadioBox(option)

    # 组合单元
    def inputChk_combination_unit(self, options):
        self.clickSingleCheckBox(options)

    # 查询
    def btn_qry(self):
        self.btn_query()

    # # 线路编号
    # def inputStr_line_no(self, content):
    #     self.input(content)
    #
    # # 线路名称
    # def inputStr_line_name(self, content):
    #     self.input(content)
    #
    # # 查询日期
    # def inputDt_query_date(self, content):
    #     self.input(content)
    #
    # # 按时间统计类型
    # def inputDt_stat_date_type(self, name):
    #     self.clickDt_Tab(name)
    #
    # # 组合单元
    # def inputChk_composition_unit(self, name):
    #     self.clickSingleCheckBox(name)
    #
    # # 线损类型
    # def inputSChk_line_loss_type(self, name):
    #     self.clickRadioBox(name)
    #
    # # 查询按钮
    # def btn_qry(self):
    #     self.btn_query()
