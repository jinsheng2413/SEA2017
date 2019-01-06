# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/11/1 13:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→时钟管理→对时结果分析
# 对时结果分析
class ClockResultStaticPage(Page):

    def inputChk_static_method(self, option):
        self.clickRadioBox(option)

    # 终端厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        # self.click(ClockResultStaticLocators.TMNL_FAC_SEL)
        # locator = self.get_select_locator(
        #     ClockResultStaticLocators.TMNL_FAC, name)
        # self.click(locator)
        self.selectDropDown(item)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *ClockResultStaticLocators.QUERY_DATE)
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        # self.click(ClockResultStaticLocators.BTN_QUERY)
        self.btn_query()


# 对时结果明细
class ClockResultDetailPage(Page):

    # 类别--打开并选择
    def inputSel_clock_model(self, item):
        self.clean_label(item)  # '类')
        self.selectDropDown(item)

    # 电表资产号
    def inputStr_met_asset_no(self, value):
        # self.input(value, *ClockResultDetailLocators.MET_ASSET_NO)
        self.input(value)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        # self.input(value, *ClockResultDetailLocators.TMNL_ASSET_NO)
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        # self.input(value, *ClockResultDetailLocators.TMNL_ADDR)
        self.input(value)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *ClockResultDetailLocators.QUERY_DATE)
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        # self.click(ClockResultDetailLocators.BTN_QUERY)
        self.btn_query(True)
