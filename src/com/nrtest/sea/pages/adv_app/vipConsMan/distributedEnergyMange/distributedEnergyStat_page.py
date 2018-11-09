# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyStat_locators import \
    DistributedEnergyStatLocators


class DistributedEnergyStatPage(Page):
    # 日期
    def inputStr_date(self, value):
        self.input(value, *DistributedEnergyStatLocators.QRY_DATE)

    # 发电量消纳方式
    def inputSel_powerConsumptionMode(self, name):
        self.click(*DistributedEnergyStatLocators.QRY_POWER_CONSUMPTION_MODE)
        locator = self.get_select_locator(
            DistributedEnergyStatLocators.QRY_POWER_CONSUMPTION_MODE_VALUE, name)
        self.click(*locator)

    # 发电方式
    def inputSel_powerMode(self, name):
        self.click(*DistributedEnergyStatLocators.QRY_POWER_MODE)
        locator = self.get_select_locator(
            DistributedEnergyStatLocators.QRY_POWER_MODE_VALUE, name)
        self.click(*locator)

    # 查询

    def btn_qry(self):
        self.click(*DistributedEnergyStatLocators.BTN_QRY)