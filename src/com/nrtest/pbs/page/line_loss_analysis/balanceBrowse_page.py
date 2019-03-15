# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: balanceBrowse_page.py
@time: 2019-03-15 10:04
@desc:
"""

from com.nrtest.pbs.locators.line_loss_analysis.balanceBrowse_locators import *
from com.nrtest.pbs.tree.tree_page import TreePBSPage


# 线损分析→母平浏览:母平汇总
class BalanceBrowseCollectPage(TreePBSPage):
    # 区域
    def inputSel_area(self, value):
        self.selectDropDown(value)

    # 时间方案
    def inputChk_date_type(self, value):
        self.click_button(value)

    # 查询按钮
    def btn_qry(self):
        self.click(BalanceBrowseCollectLocators.BTN_QRY)


# 线损分析→母平浏览:母平查询
class BalanceBrowseQueryPage(TreePBSPage):
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
        self.click(BalanceBrowseQueryLocators.BTN_QRY)
