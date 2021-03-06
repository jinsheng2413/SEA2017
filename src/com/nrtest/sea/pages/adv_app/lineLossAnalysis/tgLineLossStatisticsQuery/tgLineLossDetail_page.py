# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossDetail_page.py
@time: 2018/11/2 10:07
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossDetail_locators import \
    TgLineLossDetailLocators


# 高级应用→线损管理→台区线损统计查询→台区线损明细

class TgLineLossDetailPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content)

    # 查询日期,开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 责任人工号
    def inputStr_person_resp_no(self, content):
        self.input(content)

    # 采集覆盖率
    def inputSel_collect_cover_rate(self, value):
        self.selectDropDown(value)

    # 采集覆盖率值
    def inputStr_collect_cover_rate_input(self, value):
        self.specialInput(TgLineLossDetailLocators.QRY_INPUT, value, 1)

    # 采集覆盖率TO
    def inputSel_collect_cover_rate_to(self, option):
        self.specialDropdown(option, TgLineLossDetailLocators.QRY_SEL, 1)

    # 采集覆盖率TO值
    def inputStr_collect_cover_rate_to_input(self, value):
        self.specialInput(TgLineLossDetailLocators.QRY_INPUT, value, 2)

    # 采集成功率
    def inputSel_collect_success_rate(self, value):
        self.selectDropDown(value)

    # 采集成功率值
    def inputStr_collect_success_rate_input(self, value):
        self.specialInput(TgLineLossDetailLocators.QRY_INPUT, value, 3)

    # 采集成功率TO
    def inputSel_collect_success_rate_to(self, option):
        self.specialDropdown(option, TgLineLossDetailLocators.QRY_SEL, 2)

    # 采集成功率TO值
    def inputStr_collect_success_rate_to_input(self, value):
        self.specialInput(TgLineLossDetailLocators.QRY_INPUT, value, 4)

    # 同期线损率
    def inputSel_collecline_loss_rate(self, value):
        self.selectDropDown(value)

    # 同期线损率值
    def inputStr_collecline_loss_rate_input(self, value):
        self.specialInput(TgLineLossDetailLocators.QRY_INPUT, value, 5)

    # 同期线损率TO
    def inputSel_collecline_loss_rate_to(self, option):
        self.specialDropdown(option, TgLineLossDetailLocators.QRY_SEL, 3)

    # 同期线损率TO值
    def inputStr_collecline_loss_rate_to_input(self, value):
        self.specialInput(TgLineLossDetailLocators.QRY_INPUT, value, 6)

    # 时间类型
    def inputChk_date_type(self, value):
        self.clickRadioBox(value)

    # 运算类型
    def inputChk_compute_type(self, value):
        self.clickRadioBox(value)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
