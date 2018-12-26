# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.dataAnalyse.powerSortAnalyse_locators import PowerSortAnalyseLocators


class PowerSortAnalysePage(Page):
    # 排名数量
    def inputStr_rankingNumber(self, value):
        self.input(value)#, *PowerSortAnalyseLocators.QRY_RANKING_NUMBER)

    # 用户类型
    def inputSel_userType(self, options):
        # self.click(*PowerSortAnalyseLocators.QRY_USER_TYPE)
        # locator = self.get_select_locator(
        #     PowerSortAnalyseLocators.QRY__USER_TYPE_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options)
    # 开始时间
    def inputStr_start_time(self, value):
        self.input(value)#, *PowerSortAnalyseLocators.QRY_START_TIME)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value)#, *PowerSortAnalyseLocators.QRY_END_TIME)

        # 查询

    def btn_qry(self):
        #self.click(*PowerSortAnalyseLocators.BTN_QRY)
        self.btn_query()
