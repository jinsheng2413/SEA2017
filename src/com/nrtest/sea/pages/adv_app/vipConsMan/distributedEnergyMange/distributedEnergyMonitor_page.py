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
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 发电类型
    def inputSel_gc_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集监测明细
class DistributedEnergyMonitorDetailPage(Page):
    # 数据类型
    def inputChk_data_type(self, index):
        self.clickRadioBox(index)

    # 户号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 电能表资产编号
    def inputStr_meter_asset_no(self, content):
        self.input(content)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 发电类型
    def inputSel_gc_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集成功率
class DistributedEnergySuccessRatePage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index)

    # 开始日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源用户抄表失败明细
class DistributedEnergyUserFailedPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 电能表资产编号
    def inputStr_meter_asset_no(self, content):
        self.input(content)

    # 发电用户编号
    def inputStr_gc_cons_no(self, content):
        self.input(content)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
