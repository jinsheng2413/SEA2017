# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossBrowse_page.py
@time: 2019-03-14 15:12
@desc:
"""
from com.nrtest.common.base_page import Page


# 线损分析→线损浏览:线损汇总
class LineLossBrowseCollectPage(Page):
    # 区域
    def inputSel_area(self, value):
        self.selectDropDown(value)

    # 时间方案
    def inputChk_date_type(self, value):
        self.click_button(value)

    # 查询按钮
    def btn_qry(self):
        # self.click(LineLossBrowseCollectLocators.BTN_QRY)
        self.btn_query(is_multi_tab=True)


# 线损分析→线损浏览:线损查询
class LineLossBrowseQueryPage(Page):
    # 电压
    def inputSel_voltage(self, value):
        self.selectDropDown(value)

    # 类型
    def inputSel_type(self, value):
        self.selectDropDown(value)

    # 损耗率
    def inputSel_attrition_rate(self, value):
        self.selectDropDown(value)

    # 时间类型
    def inputChk_date_type(self, value):
        self.click_button(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
