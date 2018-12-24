# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.readIntimeRate_locators import \
    ReadIntimeRate_Locators


class ReadIntimeRatePage(Page):
    # 芯片厂家
    def inputSel_chipFactory(self, name):
        # self.click(*ReadIntimeRate_Locators.QRY_CHIP_FACTORY)
        # locator = self.get_select_locator(
        # ReadIntimeRate_Locators.QRY_CHIP_FACTORY_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)
    # 终端厂家
    def inputSel_tmnlFactory(self, name):
        # self.click(*ReadIntimeRate_Locators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(
        # ReadIntimeRate_Locators.QRY_TMNL_FACTORY_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 用户类型
    def inputSel_userType(self, name):
        # self.click(*ReadIntimeRate_Locators.QRY_USER_TYPE)
        # locator = self.get_select_locator(
        # ReadIntimeRate_Locators.QRY_USER_TYPE_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 日期时间
    def inputStr_date_time(self, value):
        # self.input(value, *ReadIntimeRate_Locators.QRY_DATE_TIME)
        self.input(value)

        # 查询

    def btn_qry(self):
        self.click(*ReadIntimeRate_Locators.BTN_QRY)
