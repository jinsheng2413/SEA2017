# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyStat_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用--》重点用户检测--》分布式电源管理--》分布式电源接入统计
class DistributedEnergyStatPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        # self.input(value, *DistributedEnergyStatLocators.QRY_DATE)
        self.inputDate(value)

    # 发电量消纳方式
    def inputSel_abso_type(self, name):
        # self.click(*DistributedEnergyStatLocators.QRY_ABSO_TYPE)
        # locator = self.get_select_locator(
        #     DistributedEnergyStatLocators.QRY_ABSO_TYPE_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 发电方式
    def inputSel_gc_type(self, name):
        # self.click(*DistributedEnergyStatLocators.QRY_GC_TYPE)
        # locator = self.get_select_locator(
        #     DistributedEnergyStatLocators.QRY_GC_TYPE_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 查询
    def btn_qry(self):
        # self.click(*DistributedEnergyStatLocators.BTN_QRY)
        self.btn_query()


# 高级应用--》重点用户检测--》分布式电源管理--》分布式电源接入明细
class DistributedEnergyStatDetailPage(Page):
    # 电能表用途
    def inputSel_meter_purpose(self, index):
        self.selectDropDown(index)

    # 发电类型
    def inputSel_gc_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 覆盖情况
    def inputSel_cover_status(self, index):
        self.selectDropDown(index)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 日期
    def inputDt_query_date(self, index):
        self.inputDate(index)

    # 台区编号
    def inputStr_tg_no(self, index):
        self.input(index)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
