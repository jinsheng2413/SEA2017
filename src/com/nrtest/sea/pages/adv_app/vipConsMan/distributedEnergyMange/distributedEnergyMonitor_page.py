# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyMonitor_page.py
@time: 2018/11/8 14:13
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测
# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集监测统计
class DistributedEnergyMonitorStatisticsPage(Page):
    # 查询日期，开始
    def inputDt_start_date(self, content):
        # self.exec_script(DistributedEnergyMonitorStatisticsLocators.START_DATE_JS)
        # self.input(content, *DistributedEnergyMonitorStatisticsLocators.QRY_START_DATE)
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        # self.exec_script(DistributedEnergyMonitorStatisticsLocators.END_DATE_JS)
        # self.input(content, *DistributedEnergyMonitorStatisticsLocators.QRY_END_DATE)
        self.inputDate(content)

    # 发电类型
    def inputSel_gc_type(self, index):
        # self.click(*DistributedEnergyMonitorStatisticsLocators.QRY_GC_TYPE)
        # locator = self.get_select_locator(
        #     DistributedEnergyMonitorStatisticsLocators.QRY_GC_TYPE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        # self.click(*DistributedEnergyMonitorStatisticsLocators.BTN_SEARCH)
        self.btn_query()

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集监测明细
class DistributedEnergyMonitorDetailPage(Page):
    # 数据类型
    def inputChk_data_type(self, index):
        self.clickRadioBox(index)

    # 户号
    def inputStr_cons_no(self, content):
        self.input(content)  #, *DistributedEnergyMonitorDetailLocators.QRY_CONS_NO)

    # 电能表资产编号
    def inputStr_meter_asset_no(self, content):
        self.input(content)  #, *DistributedEnergyMonitorDetailLocators.QRY_METER_ASSET_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *DistributedEnergyMonitorDetailLocators.QRY_TMNL_ADDR)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(DistributedEnergyMonitorDetailLocators.DATE_JS)
        # self.input(content, *DistributedEnergyMonitorDetailLocators.QRY_DATE)
        self.inputDate(content)

    # 发电类型
    def inputSel_gc_type(self, index):
        # self.click(*DistributedEnergyMonitorDetailLocators.QRY_GC_TYPE)
        # locator = self.get_select_locator(
        #     DistributedEnergyMonitorDetailLocators.QRY_GC_TYPE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        # self.click(*DistributedEnergyMonitorDetailLocators.BTN_SEARCH)
        self.btn_query(True)

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集成功率
class DistributedEnergySuccessRatePage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(*DistributedEnergySuccessRateLocators.QRY_CONS_TYPE)
        # locator = self.get_select_locator(
        #     DistributedEnergySuccessRateLocators.QRY_CONS_TYPE_VALUE, index)
        # self.click(*locator)
        self.selectCheckBox(index)

    # 开始日期
    def inputDt_start_date(self, content):
        # self.exec_script(DistributedEnergySuccessRateLocators.DATE_JS)
        # self.input(content, *DistributedEnergySuccessRateLocators.QRY_DATE)
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(*DistributedEnergySuccessRateLocators.BTN_SEARCH)
        self.btn_query(True)

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源用户抄表失败明细
class DistributedEnergyUserFailedPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        # if index == 'c':
        #     self._find_element(*DistributedEnergyUserFailedLocators.QRY_CONS_TYPE)
        # else:
        #     self.click(*DistributedEnergyUserFailedLocators.QRY_CONS_TYPE)
        #     locator = self.get_select_locator(
        #         DistributedEnergyUserFailedLocators.QRY_CONS_TYPE_VALUE, index)
        #     self.click(*locator)
        #     self.click(*DistributedEnergyUserFailedLocators.QRY_CONS_TYPE)
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 电能表资产编号
    def inputStr_meter_asset_no(self, content):
        self.input(content)  #, *DistributedEnergyUserFailedLocators.QRY_METER_ASSET_NO)

    # 发电用户编号
    def inputStr_gc_cons_no(self, content):
        self.input(content)  # , *DistributedEnergyUserFailedLocators.QRY_GC_CONS_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *DistributedEnergyUserFailedLocators.QRY_TMNL_ADDR)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(DistributedEnergyUserFailedLocators.DATE_JS)
        # self.input(content, *DistributedEnergyUserFailedLocators.QRY_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(*DistributedEnergyUserFailedLocators.BTN_SEARCH)
        self.btn_query(True)
