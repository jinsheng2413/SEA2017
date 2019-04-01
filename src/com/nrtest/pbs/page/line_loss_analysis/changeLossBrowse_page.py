# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: changeLossBrowse_page.py
@time: 2019-03-14 16:37
@desc:
"""

from com.nrtest.common.base_page import Page


# 线损分析→变损浏览:变损汇总
from com.nrtest.pbs.locators.line_loss_analysis.lineLossAnalysis_locators import LineLossAnalysis_locators


class ChangeLossBrowseCollectPage(Page):
    # 区域
    def inputSel_area(self, value):
        self.selectDropDown(value)

    # 时间方案
    def inputChk_date_type(self, value):
        self.clickDt_Tab(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)


# 线损分析→变损浏览:变损查询
class ChangeLossBrowseQueryPage(Page):
    # 电压
    def inputSel_voltage(self, value):
        self.selectDropDown(value)

    # 类型
    def inputSel_type(self, value):
        self.selectDropDown(value)

    # 损耗率
    def inputSel_attrition_rate(self,input):
        input_text = input.split(';')[2].split(',')
        # 第一个
        self.click(LineLossAnalysis_locators.A_DOWN_FIRST)
        xpath1 = self.format_xpath(LineLossAnalysis_locators.DROP_DOWN_TEXT, input_text[0])
        self.click(xpath1)
        # 第二个
        self.input(input_text[1], *LineLossAnalysis_locators.INPUT_SECOND)
        # 第三个
        self.click(LineLossAnalysis_locators.A_DOWN_SECOND)
        xpath2 = self.format_xpath(LineLossAnalysis_locators.DROP_DOWN_TEXT, input_text[2])
        self.click(xpath2)
        # 第四个
        self.click(LineLossAnalysis_locators.A_DOWN_THIRD)
        xpath3 = self.format_xpath(LineLossAnalysis_locators.DROP_DOWN_TEXT, input_text[3])
        self.click(xpath3)
        # 第五个
        self.input(input_text[4], *LineLossAnalysis_locators.INPUT_FIFTH)

    # 时间类型
    def inputChk_date_type(self, value):
        self.clickDt_Tab(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
