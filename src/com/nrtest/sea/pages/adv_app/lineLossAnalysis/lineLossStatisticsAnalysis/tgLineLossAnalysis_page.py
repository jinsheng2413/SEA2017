# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossAnalysis_page.py
@time: 2018/10/30 13:59
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.tgLineLossAnalysis_locators import \
    TgLineLossAnalysisLocators


# 高级应用→线损管理→线损统计分析→台区线损分析
class TgLineLossAnalysisPage(Page):
    # 安装率
    def inputSel_install_rate(self, option):
        self.clean_label(option)
        self.selectDropDown(option)

    # 安装率值
    def inputStr_install_rate_input(self, value):
        # 页面元素位置变动时，会存在定位错误问题，需人工调整
        self.specialInput(TgLineLossAnalysisLocators.QRY_INPUT, value, 1)

    # 安装率TO
    def inputSel_install_rate_to(self, option):
        self.specialDropdown(option, TgLineLossAnalysisLocators.QRY_SEL, 1)

    # 安装率TO值
    def inputStr_install_rate_to_input(self, value):
        self.specialInput(TgLineLossAnalysisLocators.QRY_INPUT, value, 2)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 抄读成功率
    def inputSel_read_success_rate(self, option):
        self.clean_label(option)
        self.selectDropDown(option)

    # 抄读成功率值
    def inputStr_read_success_rate_input(self, value):
        self.specialInput(TgLineLossAnalysisLocators.QRY_INPUT, value, 3)

    # 抄读成功率TO
    def inputSel_read_success_rate_to(self, option):
        self.specialDropdown(option, TgLineLossAnalysisLocators.QRY_SEL, 2)

    # 抄读成功率TO值
    def inputStr_read_success_rate_to_input(self, value):
        self.specialInput(TgLineLossAnalysisLocators.QRY_INPUT, value, 4)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 线损率
    def inputSel_line_loss_rate(self, option):
        self.clean_label(option)
        self.selectDropDown(option)

    # 线损率值
    def inputStr_line_loss_rate_input(self, value):
        self.specialInput(TgLineLossAnalysisLocators.QRY_INPUT, value, 5)

    # 线损率TO
    def inputSel_line_loss_rate_to(self, option):
        self.specialDropdown(option, TgLineLossAnalysisLocators.QRY_SEL, 3)

    # 线损率TO值
    def inputStr_line_loss_rate_to_input(self, value):
        self.specialInput(TgLineLossAnalysisLocators.QRY_INPUT, value, 6)

    # 是否可算
    def inputChk_is_can_calc(self, option):
        self.clickRadioBox(option)

    # 可算分类
    def inputChk_can_calc_type(self, option):
        self.clickRadioBox(option)

    # 按日期类型
    def inputChk_qry_date_type(self, option):
        self.clickDt_Tab(option)

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
