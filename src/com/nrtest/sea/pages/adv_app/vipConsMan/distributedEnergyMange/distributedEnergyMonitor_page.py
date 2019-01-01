# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyMonitor_page.py
@time: 2018/11/8 14:13
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyMonitor_locators import *


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测
# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集监测统计
class DistributedEnergyMonitorStatisticsPage(Page):
    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.exec_script(DistributedEnergyMonitorStatisticsLocators.START_DATE_JS)
        self.input(content, *DistributedEnergyMonitorStatisticsLocators.QRY_START_DATE)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.exec_script(DistributedEnergyMonitorStatisticsLocators.END_DATE_JS)
        self.input(content, *DistributedEnergyMonitorStatisticsLocators.QRY_END_DATE)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(DistributedEnergyMonitorStatisticsLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyMonitorStatisticsLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search(self):
        self.click(DistributedEnergyMonitorStatisticsLocators.BTN_SEARCH)


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集监测明细
class DistributedEnergyMonitorDetailPage(Page):
    # 户号
    def inputStr_cons_no(self, content):
        self.input(content, *DistributedEnergyMonitorDetailLocators.QRY_CONS_NO)

    # 电能表资产编号
    def inputStr_meter_asset_no(self, content):
        self.input(content, *DistributedEnergyMonitorDetailLocators.QRY_METER_ASSET_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *DistributedEnergyMonitorDetailLocators.QRY_TMNL_ADDR)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyMonitorDetailLocators.DATE_JS)
        self.input(content, *DistributedEnergyMonitorDetailLocators.QRY_DATE)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(DistributedEnergyMonitorDetailLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyMonitorDetailLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search(self):
        self.click(DistributedEnergyMonitorDetailLocators.BTN_SEARCH)


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集成功率
class DistributedEnergySuccessRatePage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.click(DistributedEnergySuccessRateLocators.QRY_CONS_TYPE)
        locator = self.get_select_locator(
            DistributedEnergySuccessRateLocators.QRY_CONS_TYPE_VALUE, index)
        self.click(locator)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergySuccessRateLocators.DATE_JS)
        self.input(content, *DistributedEnergySuccessRateLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(DistributedEnergySuccessRateLocators.BTN_SEARCH)


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源用户抄表失败明细
class DistributedEnergyUserFailedPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        if index == 'c':
            self._find_element(DistributedEnergyUserFailedLocators.QRY_CONS_TYPE)
        else:
            self.click(DistributedEnergyUserFailedLocators.QRY_CONS_TYPE)
            locator = self.get_select_locator(
                DistributedEnergyUserFailedLocators.QRY_CONS_TYPE_VALUE, index)
            self.click(locator)
            self.click(DistributedEnergyUserFailedLocators.QRY_CONS_TYPE)

    # 电能表资产编号
    def inputStr_meter_asset_no(self, content):
        self.input(content, *DistributedEnergyUserFailedLocators.QRY_METER_ASSET_NO)

    # 发电用户编号
    def inputStr_energy_user_no(self, content):
        self.input(content, *DistributedEnergyUserFailedLocators.QRY_ENERGY_USER_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *DistributedEnergyUserFailedLocators.QRY_TMNL_ADDR)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyUserFailedLocators.DATE_JS)
        self.input(content, *DistributedEnergyUserFailedLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(DistributedEnergyUserFailedLocators.BTN_SEARCH)
