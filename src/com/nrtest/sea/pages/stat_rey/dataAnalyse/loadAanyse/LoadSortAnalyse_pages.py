# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.dataAnalyse.loadAanyse.loadSortAnalyse_locators import LoadSortAnalyseLocators


class LoadSortAnalysePage(Page):
    # 开始日期
    def inputStr_startDate(self, value):
        self.input(value, *LoadSortAnalyseLocators.QRY_START_DATE)

    # 用户类型
    def inputSel_userType(self, name):
        self.click(*LoadSortAnalyseLocators.QRY_USER_TYPE)
        locator = self.get_select_locator(LoadSortAnalyseLocators.QRY_USER_TYPE_VALUE, name)
        self.click(*locator)

    # 结束日期
    def inputStr_end_time(self, value):
        self.input(value, *LoadSortAnalyseLocators.QRY_END_DATE)

    # 排名数量
    def inputStr_anking_number(self, value):
        self.input(value, *LoadSortAnalyseLocators.QRY_RANKING_NUMBER)

    # 查询
    def btn_qry(self):
        self.click(*LoadSortAnalyseLocators.BTN_QRY)
