# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: balanceBrowse_page.py
@time: 2019-03-15 10:04
@desc:
"""

from com.nrtest.common.base_page import Page


# 线损分析→母平浏览:母平汇总
from com.nrtest.pbs.locators.line_loss_analysis.lineLossAnalysis_locators import LineLossAnalysis_locators


class BalanceBrowseCollectPage(Page):
    # 区域
    def inputSel_area(self, value):
        self.specialDropdown(value,locator=LineLossAnalysis_locators.DROP_DOWN_AREA)

    # 时间方案
    def inputChk_date_type(self, value):
        self.clickDt_Tab(value)

    def inputDt_date(self,value):
        self.inputDate(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)


# 线损分析→母平浏览:母平查询
class BalanceBrowseQueryPage(Page):
    # 电压
    def inputSel_voltage(self, value):
        self.selectDropDown(value)

    # 类型
    def inputSel_type(self, value):
        self.selectDropDown(value)

    # 损耗率
    def inputSel_attrition_rate_first(self,option):
        self.specialDropdown(option,locator=LineLossAnalysis_locators.A_DOWN_FIRST)
        # input_text = input.split(';')[2].split(',')
        # # 第一个
        # self.click(LineLossAnalysis_locators.A_DOWN_FIRST)
        # xpath1 = self.format_xpath(LineLossAnalysis_locators.DROP_DOWN_TEXT, input_text[0])
        # self.click(xpath1)
        # # 第二个
        # self.input(input_text[1], *LineLossAnalysis_locators.INPUT_SECOND)
        # # 第三个
        # self.click(LineLossAnalysis_locators.A_DOWN_SECOND)
        # xpath2 = self.format_xpath(LineLossAnalysis_locators.DROP_DOWN_TEXT, input_text[2])
        # self.click(xpath2)
        # # 第四个
        # self.click(LineLossAnalysis_locators.A_DOWN_THIRD)
        # xpath3 = self.format_xpath(LineLossAnalysis_locators.DROP_DOWN_TEXT, input_text[3])
        # self.click(xpath3)
        # # 第五个
        # self.input(input_text[4], *LineLossAnalysis_locators.INPUT_FIFTH)
        # 损耗率

    def inputStr_attrition_rate_second(self, option):
        value = self.get_para_value(option)
        self.input(value, *LineLossAnalysis_locators.INPUT_SECOND)

    def inputSel_attrition_rate_third(self, option):
        self.specialDropdown(option, locator=LineLossAnalysis_locators.A_DOWN_SECOND)

    # 损耗率
    def inputSel_attrition_rate_fourth(self, option):
        self.specialDropdown(option, locator=LineLossAnalysis_locators.A_DOWN_THIRD)

    # 损耗率
    def inputStr_attrition_rate_fifth(self, option):
        value = self.get_para_value(option)
        self.input(value, *LineLossAnalysis_locators.INPUT_SECOND)

    # 时间类型
    def inputChk_date_type(self, value):
        self.clickDt_Tab(value)
    #时间
    def inputDt_query_time(self,value):
        self.inputDate(value,locators=LineLossAnalysis_locators.LINE_LOSS_TIME)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
