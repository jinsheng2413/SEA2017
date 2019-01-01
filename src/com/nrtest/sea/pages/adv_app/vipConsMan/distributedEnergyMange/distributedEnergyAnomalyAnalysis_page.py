# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyAnomalyAnalysis_page.py
@time: 2018/11/9 15:01
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyAnomalyAnalysis_locators import *


# 高级应用→重点用户监测→分布式电源管理→分布式电源异常分析
class DistributedEnergyAnomalyAnalysisPage(Page):
    # 日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyAnomalyAnalysisLocators.DATE_JS)
        self.input(content, *DistributedEnergyAnomalyAnalysisLocators.QRY_DATE)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(DistributedEnergyAnomalyAnalysisLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyAnomalyAnalysisLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(locator)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.click(DistributedEnergyAnomalyAnalysisLocators.QRY_ABSO_MODE)
        locator = self.get_select_locator(
            DistributedEnergyAnomalyAnalysisLocators.QRY_ABSO_MODE_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search(self):
        self.click(DistributedEnergyAnomalyAnalysisLocators.BTN_SEARCH)


# 高级应用→重点用户监测→分布式电源管理→分布式电源异常分析→分布式电源异常情况明细
class DistributedEnergyAnomalyDetailPage(Page):
    # 日期
    def inputDt_date(self, content):
        self.exec_script(DistributedEnergyAnomalyDetailLocators.DATE_JS)
        self.input(content, *DistributedEnergyAnomalyDetailLocators.QRY_DATE)

    # 异常类型
    def inputSel_anomaly_type(self, index):
        self.click(DistributedEnergyAnomalyDetailLocators.QRY_ANOMALY_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyAnomalyDetailLocators.QRY_ANOMALY_TYPE_VALUE, index)
        self.click(locator)

    # 发电类型
    def inputSel_elec_type(self, index):
        self.click(DistributedEnergyAnomalyDetailLocators.QRY_ELEC_TYPE)
        locator = self.get_select_locator(
            DistributedEnergyAnomalyDetailLocators.QRY_ELEC_TYPE_VALUE, index)
        self.click(locator)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.click(DistributedEnergyAnomalyDetailLocators.QRY_ABSO_MODE)
        locator = self.get_select_locator(
            DistributedEnergyAnomalyDetailLocators.QRY_ABSO_MODE_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search(self):
        self.click(DistributedEnergyAnomalyDetailLocators.BTN_SEARCH)
