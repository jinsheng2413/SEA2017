# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: indexAllocation_page.py
@time: 2018/11/2 14:15
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.personalizedIndexDisplay.indexAllocation_locators import \
    IndexAllocationLocators


# 高级应用→线损分析→同期线损→指标配置
class IndexAllocationPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content, *IndexAllocationLocators.QRY_TG_NO)

    # 台区状态
    def inputSel_tg_status(self, index):
        self.click(*IndexAllocationLocators.QRY_TG_STATUS)
        locator = self.get_select_locator(
            IndexAllocationLocators.QRY_TG_STATUS_VALUE, index)
        self.click(*locator)

    # 责任人工号
    def inputStr_charge_person_no(self, content):
        self.input(content, *IndexAllocationLocators.QRY_CHARGE_PERSON_NO)

    # 查询按钮
    def btn_search(self):
        self.click(*IndexAllocationLocators.BTN_SEARCH)
