# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→数据分析→电量分析→电量数据查询
class GisPanoramaDisplayPage(Page):
    # 逐日显示
    def inputStr_day_display(self, value):
        # self.click(GisPanoramaDisplayLocators.QRY_DAY_DISPLAY)
        # locator = self.get_select_locator(
        #     GisPanoramaDisplayLocators.QRY_USER_TYPE_VALUE, value)
        # self.click(locator)
        self.selectDropDown(value)

    # 用户类型
    def inputSel_userType(self, name):
        # self.click(GisPanoramaDisplayLocators.QRY_USER_TYPE)
        # locator = self.get_select_locator(
        #     GisPanoramaDisplayLocators.QRY_USER_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 查询时间
    def inputDt_query_time(self, value):
        # self.input(value, *GisPanoramaDisplayLocators.QRY_QUERY_TIME)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(GisPanoramaDisplayLocators.BTN_QRY)
        self.btn_query()
