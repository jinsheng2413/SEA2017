# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossStatisticsQuery_page.py
@time: 2018/10/31 14:44
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→线损统计分析→线损统计查询


class LineLossStatisticsQueryPage(Page):
    day = 0
    month = 0
    year = 0
    # 线损分类
    def inputSel_line_loss_type(self, index):
        # self.click(LineLossStatisticsQueryLocators.QRY_LINE_LOSS_TYPE)
        # locator = self.get_select_locator(
        #     LineLossStatisticsQueryLocators.QRY_LINE_LOSS_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 线损率
    def inputSel_line_loss_rate(self, index):
        # self.click(LineLossStatisticsQueryLocators.QRY_LINE_LOSS_RATE)
        # locator = self.get_select_locator(
        #     LineLossStatisticsQueryLocators.QRY_LINE_LOSS_RATE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    def inputStr_line_loss_rate(self, content):
        # self.input(
        #     content, *LineLossStatisticsQueryLocators.QRY_LINE_LOSS_RATE_INPUT)
        self.input(content)

    # 日期
    def inputDt_date(self, content):
        # self.exec_script(LineLossStatisticsQueryLocators.DATE_JS)
        # self.input(content, *LineLossStatisticsQueryLocators.QRY_DATE)
        self.inputDate(content)

    # 起
    def inputDT_from(self, name):
        self.inputDate(name)

    # 止
    def inputDT_to(self, name):
        self.input(name)

    # 按底码
    def inputChk_code(self, name):
        self.clickSingleCheckBox(name)

    # 月
    def inputChl_qryType_month(self, name):
        self.clickSingleCheckBox(name)
        self.month = 1

    # 日
    def inputChl_qryType_day(self, name):
        self.clickSingleCheckBox(name)
        self.day = 1


    # 查询按钮
    def btn_search(self):
        # self.click(LineLossStatisticsQueryLocators.BTN_SEARCH)
        self.clean_btn('查')
        self.btn_query(True)
