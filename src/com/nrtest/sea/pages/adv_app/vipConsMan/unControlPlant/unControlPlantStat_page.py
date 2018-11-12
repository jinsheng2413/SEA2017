# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: unControlPlantStat_page.py
@time: 2018/11/12 11:14
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.unControlPlant.unControlPlantStat_locators import *


# 高级应用→重点用户监测→非统调电厂管理→非统调电厂接入统计
class UnControlPlantStatPage(Page):
    # 发电方式
    def inputSel_elec_way(self, index):
        self.click(*UnControlPlantStatLocators.QRY_ELEC_WAY)
        locator = self.get_select_locator(UnControlPlantStatLocators.QRY_ELEC_WAY_VALUE, index)
        self.click(*locator)

    # 采集方式
    def inputSel_gather_way(self, index):
        self.click(*UnControlPlantStatLocators.QRY_GATHER_WAY)
        locator = self.get_select_locator(UnControlPlantStatLocators.QRY_GATHER_WAY_VALUE, index)
        self.click(*locator)

    # 日期
    def inputDt_date(self, content):
        self.exec_script(UnControlPlantStatLocators.DATE_JS)
        self.input(content, *UnControlPlantStatLocators.QRY_DATE)

    # 查询
    def btn_search(self):
        self.click(*UnControlPlantStatLocators.BTN_SEARCH)


# 高级应用→重点用户监测→非统调电厂管理→非统调电厂接入统计→非统调电厂接入明细
class UnControlPlantDetailPage(Page):
    # 发电方式
    def inputSel_elec_way(self, index):
        self.click(*UnControlPlantDetailLocators.QRY_ELEC_WAY)
        locator = self.get_select_locator(UnControlPlantDetailLocators.QRY_ELEC_WAY_VALUE, index)
        self.click(*locator)

    # 采集方式
    def inputSel_gather_way(self, index):
        self.click(*UnControlPlantDetailLocators.QRY_GATHER_WAY)
        locator = self.get_select_locator(UnControlPlantDetailLocators.QRY_GATHER_WAY_VALUE, index)
        self.click(*locator)

    # 统计日期
    def inputDt_date(self, content):
        self.exec_script(UnControlPlantDetailLocators.DATE_JS)
        self.input(content, *UnControlPlantDetailLocators.QRY_DATE)

    # 户号
    def inputStr_cons_no(self, content):
        self.input(content, *UnControlPlantDetailLocators.QRY_CONS_NO)

    # 表资产编号
    def inputStr_meter_asset_no(self, content):
        self.input(content, *UnControlPlantDetailLocators.QRY_METER_ASSET_NO)

    # 终端资产编号
    def inputStr_tmnl_addr(self, content):
        self.input(content, *UnControlPlantDetailLocators.QRY_TMNL_ASSET_NO)

    # 查询
    def btn_search(self):
        self.click(*UnControlPlantDetailLocators.BTN_SEARCH)
