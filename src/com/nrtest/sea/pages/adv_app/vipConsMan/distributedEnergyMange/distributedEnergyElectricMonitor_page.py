# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyElectricMonitor_page.py
@time: 2018/11/9 16:52
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyElectricMonitor_locators import *


# 高级应用→重点用户监测→分布式电源管理→分布式电源电量监测→分布式电源电量趋势
class DistributedEnergyElectricTrendPage(Page):
    # 月份
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyElectricTrendLocators.DATE_JS)
        self.input(content, *DistributedEnergyElectricTrendLocators.QRY_DATE)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(*DistributedEnergyElectricTrendLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyElectricTrendLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(*locator)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.click(*DistributedEnergyElectricTrendLocators.QRY_ABSO_MODE)
        locator = self.get_select_locator(
            DistributedEnergyElectricTrendLocators.QRY_ABSO_MODE_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*DistributedEnergyElectricTrendLocators.BTN_SEARCH)


# 高级应用→重点用户监测→分布式电源管理→分布式电源电量监测→分布式电源电量监测统计
class DistributedEnergyElectricStatPage(Page):
    # 日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyElectricStatLocators.DATE_JS)
        self.input(content, *DistributedEnergyElectricStatLocators.QRY_DATE)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(*DistributedEnergyElectricStatLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyElectricStatLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(*locator)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.click(*DistributedEnergyElectricStatLocators.QRY_ABSO_MODE)
        locator = self.get_select_locator(
            DistributedEnergyElectricStatLocators.QRY_ABSO_MODE_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*DistributedEnergyElectricStatLocators.BTN_SEARCH)


# 高级应用→重点用户监测→分布式电源管理→分布式电源电量监测→分布式电源电量监测明细
class DistributedEnergyElectricDetailPage(Page):
    # 电能表用途
    def inputSel_meter_purpose(self, index):
        self.click(*DistributedEnergyElectricDetailLocators.QRY_METER_PURPOSE)
        locator = self.get_select_locator(
            DistributedEnergyElectricDetailLocators.QRY_METER_PURPOSE_VALUE, index)
        self.click(*locator)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.click(*DistributedEnergyElectricDetailLocators.QRY_ABSO_MODE)
        locator = self.get_select_locator(
            DistributedEnergyElectricDetailLocators.QRY_ABSO_MODE_VALUE, index)
        self.click(*locator)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(*DistributedEnergyElectricDetailLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyElectricDetailLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(*locator)

    # 日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyElectricDetailLocators.DATE_JS)
        self.input(content, *DistributedEnergyElectricDetailLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*DistributedEnergyElectricDetailLocators.BTN_SEARCH)


# 高级应用→重点用户监测→分布式电源管理→分布式电源电量监测→分布式电源抄表示数查询
class DistributedEnergyQueryPage(Page):
    # 电能表用途
    def inputSel_meter_purpose(self, index):
        self.click(*DistributedEnergyQueryLocators.QRY_METER_PURPOSE)
        locator = self.get_select_locator(
            DistributedEnergyQueryLocators.QRY_METER_PURPOSE_VALUE, index)
        self.click(*locator)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(*DistributedEnergyQueryLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyQueryLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(*locator)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.click(*DistributedEnergyQueryLocators.QRY_ABSO_MODE)
        locator = self.get_select_locator(
            DistributedEnergyQueryLocators.QRY_ABSO_MODE_VALUE, index)
        self.click(*locator)

    # 开始日期
    def inputDt_start_date(self, content):
        self.exec_script(DistributedEnergyQueryLocators.START_DATE_JS)
        self.input(content, *DistributedEnergyQueryLocators.QRY_START_DATE)

    # 结束日期
    def inputDt_end_date(self, content):
        self.exec_script(DistributedEnergyQueryLocators.END_DATE_JS)
        self.input(content, *DistributedEnergyQueryLocators.QRY_END_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*DistributedEnergyQueryLocators.BTN_SEARCH)
