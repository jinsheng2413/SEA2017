# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: indexDetail_page.py
@time: 2018/11/2 15:00
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.personalizedIndexDisplay.indexDetail_locators import \
    IndexDetailLocators


# 高级应用→线损分析→同期线损→指标明细
class IndexDetailPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content, *IndexDetailLocators.QRY_TG_NO)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content, *IndexDetailLocators.QRY_TG_NAME)

    # 时间选择
    def inputDt_date(self, content):
        self.exec_script(IndexDetailLocators.DATE_JS)
        self.input(content, *IndexDetailLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*IndexDetailLocators.BTN_SEARCH)
