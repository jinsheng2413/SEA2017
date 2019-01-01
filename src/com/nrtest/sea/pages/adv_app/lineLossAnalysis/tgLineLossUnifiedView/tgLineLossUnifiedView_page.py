# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossUnifiedView_page.py
@time: 2018/11/1 13:55
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.tgLineLossUnifiedView.tgLineLossUnifiedView_locators import \
    TgLineLossUnifiedViewLocators


# 高级应用→线损分析→台区线损统一视图→台区线损统一视图
class TgLineLossUnifiedViewPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content, *TgLineLossUnifiedViewLocators.QRY_TG_NO)

    # 查询按钮
    def btn_search(self):
        self.click(TgLineLossUnifiedViewLocators.BTN_SEARCH)

    # 日线损
    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.exec_script(TgLineLossUnifiedViewLocators.START_DATE_JS)
        self.input(content, *TgLineLossUnifiedViewLocators.QRY_START_DATE)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.exec_script(TgLineLossUnifiedViewLocators.END_DATE_JS)
        self.input(content, *TgLineLossUnifiedViewLocators.QRY_END_DATE)

    # 查询按钮
    def btn_search_day(self):
        self.click(TgLineLossUnifiedViewLocators.BTN_SEARCH_DAY)

    # 月线损
    # 查询日期，开始
    def inputDt_start_date_tab(self, content):
        self.exec_script(TgLineLossUnifiedViewLocators.START_DATE_TAB_JS)
        self.input(content, *TgLineLossUnifiedViewLocators.QRY_START_DATE_TAB)

    # 查询日期，结束
    def inputDt_end_date_tab(self, content):
        self.exec_script(TgLineLossUnifiedViewLocators.END_DATE_TAB_JS)
        self.input(content, *TgLineLossUnifiedViewLocators.QRY_END_DATE_TAB)

    # 查询按钮
    def btn_search_month(self):
        self.click(TgLineLossUnifiedViewLocators.BTN_SEARCH_MONTH)
