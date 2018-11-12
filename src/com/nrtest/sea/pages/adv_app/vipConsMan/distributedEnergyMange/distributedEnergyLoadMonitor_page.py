# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyLoadMonitor_page.py
@time: 2018/11/12 10:27
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyLoadMonitor_locators import *


# 高级应用→重点用户监测→分布式电源管理→分布式电源负荷监测
class DistributedEnergyLoadMonitorPage(Page):
    # 日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyLoadMonitorLocators.DATE_JS)
        self.input(content, *DistributedEnergyLoadMonitorLocators.QRY_DATE)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(*DistributedEnergyLoadMonitorLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyLoadMonitorLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(*locator)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.click(*DistributedEnergyLoadMonitorLocators.QRY_ABSO_MODE)
        locator = self.get_select_locator(
            DistributedEnergyLoadMonitorLocators.QRY_ABSO_MODE_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*DistributedEnergyLoadMonitorLocators.BTN_SEARCH)


# 高级应用→重点用户监测→分布式电源管理→分布式电源负荷监测→分布式电源负荷监测明细
class DistributedEnergyLoadMonitorDetailPage(Page):
    # 电能表用途
    def inputSel_meter_purpose(self, index):
        self.click(*DistributedEnergyLoadMonitorDetailLocators.QRY_METER_PURPOSE)
        locator = self.get_select_locator(
            DistributedEnergyLoadMonitorDetailLocators.QRY_METER_PURPOSE_VALUE, index)
        self.click(*locator)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(*DistributedEnergyLoadMonitorDetailLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyLoadMonitorDetailLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(*locator)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.click(*DistributedEnergyLoadMonitorDetailLocators.QRY_ABSO_MODE)
        locator = self.get_select_locator(
            DistributedEnergyLoadMonitorDetailLocators.QRY_ABSO_MODE_VALUE, index)
        self.click(*locator)

    # 日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyLoadMonitorDetailLocators.DATE_JS)
        self.input(content, *DistributedEnergyLoadMonitorDetailLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*DistributedEnergyLoadMonitorDetailLocators.BTN_SEARCH)
