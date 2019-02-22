# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyQuality_page.py
@time: 2018/11/9 11:30
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率趋势
class SuccessRateTrendPage(Page):
    # 查询类型
    def inputChk_qry_date_type(self, index):
        self.clickRadioBox(index)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 本地通讯方式
    def inputSel_comm_mode(self, index):
        self.selectDropDown(index)

    # 远程通讯方式
    def inputSel_coll_mode(self, index):
        self.selectDropDown(index)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.selectDropDown(index)

    # 发电类型
    def inputSel_gc_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

    # 成功率类型
    def inputChk_success_type(self, index):
        self.clickRadioBox(index)

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率统计
class SuccessRateStatisticsPage(Page):
    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 本地通讯方式
    def inputSel_comm_mode(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 远程通讯方式
    def inputSel_coll_mode(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 发电类型
    def inputSel_gc_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率明细
class SuccessRateDetailPage(Page):
    # 电能表用途
    def inputSel_meter_purpose(self, index):
        self.selectDropDown(index)

    # 发电类型
    def inputSel_gc_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
