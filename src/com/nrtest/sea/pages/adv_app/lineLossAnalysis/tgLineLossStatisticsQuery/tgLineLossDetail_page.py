# -*- coding:utf-8 -*-

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


# 高级应用→线损分析→台区线损统计查询→台区线损明细
class TgLineLossDetailPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content, *TgLineLossDetailLocators.QRY_TG_NO)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content, *TgLineLossDetailLocators.QRY_TG_NAME)

    # 查询日期,开始
    def inputDt_start_date(self, content):
        self.exec_script(TgLineLossDetailLocators.START_DATE_JS)
        self.input(content, *TgLineLossDetailLocators.QRY_START_DATE)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.exec_script(TgLineLossDetailLocators.END_DATE_JS)
        self.input(content, *TgLineLossDetailLocators.QRY_END_DATE)

    # 责任人工号
    def inputStr_charge_person_no(self, content):
        self.input(content, *TgLineLossDetailLocators.QRY_CHARGE_PERSON_NO)

    # 查询按钮
    def btn_search(self):
        self.click(*TgLineLossDetailLocators.BTN_SEARCH)
