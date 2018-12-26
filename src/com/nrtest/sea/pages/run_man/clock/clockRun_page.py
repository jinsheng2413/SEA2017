# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.clock.clockRun_locators import FrequentlyCheckMetLocators
from com.nrtest.sea.locators.run_man.clock.clockRun_locators import FrequentlyCheckTmnlLocators
from com.nrtest.sea.locators.run_man.clock.clockRun_locators import StaticByFacLocators
from com.nrtest.sea.locators.run_man.clock.clockRun_locators import StaticByOrgLocators


# 运行管理→时钟管理→时钟运行质量分析
# 按单位统计
class StaticByOrgPage(Page):

    # 终端厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        # self.click(*StaticByOrgLocators.TMNL_FAC_SEL)
        # locator = self.get_select_locator(StaticByOrgLocators.TMNL_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 电能表厂商--打开并选择
    def inputSel_met_fac(self, item):
        # self.click(*StaticByOrgLocators.MET_FAC_SEL)
        # locator = self.get_select_locator(StaticByOrgLocators.MET_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *StaticByOrgLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*StaticByOrgLocators.BTN_QUERY)
        self.btn_query()

# 按厂家统计
class StaticByFacPage(Page):

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *StaticByFacLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*StaticByFacLocators.BTN_QUERY)
        self.btn_query()

# 频繁对时终端
class FrequentlyCheckTmnlPage(Page):

    # 终端类型--打开并选择
    def inputSel_tmnl_type(self, item):
        # self.click(*FrequentlyCheckTmnlLocators.TMNL_TYPE_SEL)
        # locator = self.get_select_locator(
        #     FrequentlyCheckTmnlLocators.TMNL_TYPE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 终端型号
    def inputStr_tmnl_model(self, value):
        # self.input(value, *FrequentlyCheckTmnlLocators.TMNL_MODEL)
        self.input(value)

    # 终端厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        # self.click(*FrequentlyCheckTmnlLocators.TMNL_FAC_SEL)
        # locator = self.get_select_locator(
        #     FrequentlyCheckTmnlLocators.TMNL_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        # self.input(value, *FrequentlyCheckTmnlLocators.TMNL_ASSET_NO)
        self.input(value)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *FrequentlyCheckTmnlLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*FrequentlyCheckTmnlLocators.BTN_QUERY)
        self.btn_query()

# 频繁对时电表
class FrequentlyCheckMetPage(Page):

    # 电能表厂商--打开并选择
    def inputSel_met_fac(self, item):
        # self.click(*FrequentlyCheckMetLocators.MET_FAC_SEL)
        # locator = self.get_select_locator(
        #     FrequentlyCheckMetLocators.MET_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 电表类别--打开并选择
    def inputSel_met_type(self, item):
        # self.click(*FrequentlyCheckMetLocators.MET_TYPE_SEL)
        # locator = self.get_select_locator(
        #     FrequentlyCheckMetLocators.MET_TYPE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 电能表资产号
    def inputStr_met_asset_no(self, value):
        # self.input(value, *FrequentlyCheckMetLocators.MET_ASSET_NO)
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        # self.input(value, *FrequentlyCheckMetLocators.CONS_NO)
        self.input(value)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *FrequentlyCheckMetLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*FrequentlyCheckMetLocators.BTN_QUERY)
        self.btn_query()
