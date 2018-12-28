# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→时钟管理→终端对时
# 终端对时统计
class TmnlClockStaticPage(Page):

    # 终端类型--打开并选择
    def inputSel_tmnl_type(self, item):
        # self.click(*TmnlClockStaticLocators.TMNL_TYPE_SEL)
        # locator = self.get_select_locator(
        #     TmnlClockStaticLocators.TMNL_TYPE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 终端厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        # self.click(*TmnlClockStaticLocators.TMNL_FAC_SEL)
        # locator = self.get_select_locator(
        #     TmnlClockStaticLocators.TMNL_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *TmnlClockStaticLocators.QUERY_DATE)
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*TmnlClockStaticLocators.BTN_QUERY)
        self.btn_query()


# 终端时钟明细
class TmnlClockDetailPage(Page):

    # 偏差范围--打开并选择
    def inputSel_offset_range(self, item):
        # self.click(*TmnlClockDetailLocators.OFFSET_RANGE_SEL)
        # locator = self.get_select_locator(
        #     TmnlClockDetailLocators.OFFSET_RANGE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 终端类型--打开并选择
    def inputSel_tmnl_type(self, item):
        # self.click(*TmnlClockDetailLocators.TMNL_TYPE_SEL)
        # locator = self.get_select_locator(
        #     TmnlClockDetailLocators.TMNL_TYPE, name)
        # self.click(*locator)
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 终端型号
    def inputStr_tmnl_model(self, value):
        # self.input(value, *TmnlClockDetailLocators.TMNL_MODEL)
        self.input(value)

    # 终端厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        # self.click(*TmnlClockDetailLocators.TMNL_FAC_SEL)
        # locator = self.get_select_locator(
        #     TmnlClockDetailLocators.TMNL_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        # self.input(value, *TmnlClockDetailLocators.TMNL_ADDR)
        self.input(value)

    # 是否在线--打开并选择
    def inputSel_is_online(self, item):
        # self.click(*TmnlClockDetailLocators.IS_ONLINE_SEL)
        # locator = self.get_select_locator(
        #     TmnlClockDetailLocators.IS_ONLINE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *TmnlClockDetailLocators.QUERY_DATE)
        self.inputDate(value)

    # 对时结果-打开并选择
    def inputSel_call_status(self, item):
        # self.click(*TmnlClockDetailLocators.CALL_STATUS_SEL)
        # locator = self.get_select_locator(
        #     TmnlClockDetailLocators.CALL_STATUS, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 点击查询
    def btn_qry(self):
        # self.click(*TmnlClockDetailLocators.BTN_QUERY)
        self.btn_query(True)

# 自动对时策略配置
class AutoCheckPolicyPage(Page):

    # 间隔周期--打开并选择
    def inputSel_interval_cycle(self, item):
        # self.click(*AutoCheckPolicyLocators.INTERVAL_CYCLE_SEL)
        # locator = self.get_select_locator(
        #     AutoCheckPolicyLocators.INTERVAL_CYCLE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 周期内自动对时次数--打开并选择
    def inputSel_auto_times(self, item):
        # self.click(*AutoCheckPolicyLocators.AUTO_TIMES_SEL)
        # locator = self.get_select_locator(
        #     AutoCheckPolicyLocators.AUTO_TIMES, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *AutoCheckPolicyLocators.QUERY_DATE)
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*AutoCheckPolicyLocators.BTN_QUERY)
        self.btn_query(True)
