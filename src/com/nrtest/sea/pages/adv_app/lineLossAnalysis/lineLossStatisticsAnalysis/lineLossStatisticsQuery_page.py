# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossStatisticsQuery_page.py
@time: 2018/10/31 14:44
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损管理→线损统计分析→线损统计查询
class LineLossStatisticsQueryPage(Page):
    # 线损分类
    def inputSel_line_loss_type(self, index):
        self.selectDropDown(index)

    # tab选择
    def inputChk_tab_name(self, value):
        self.clickTabPage(value)

    # 线损率
    def inputSel_line_loss_rate(self, index):
        self.selectDropDown(index)

    # 线损率值
    def inputStr_line_loss_rate_input(self, value):
        self.noLabelInput(value)
        # self.input(value)

    # 日期查询方式
    def inputChk_qry_date_type(self, value):
        self.clickRadioBox(value)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 起
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 止
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 按底码
    def inputChk_read_value(self, name):
        self.clickSingleCheckBox(name)

    # 查询按钮
    def btn_qry(self):
        self.clean_btn('查')
        self.btn_query(True)
