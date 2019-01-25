# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyAnomalyAnalysis_page.py
@time: 2018/11/9 15:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→重点用户监测→分布式电源管理→分布式电源异常分析
class DistributedEnergyAnomalyAnalysisPage(Page):
    # 查询类型
    def inputChk_qry_type(self, index):
        self.clickRadioBox(index)

    # 日期
    def inputDt_query_date(self, content):
        # self.exec_script(DistributedEnergyAnomalyAnalysisLocators.DATE_JS)
        # self.input(content, *DistributedEnergyAnomalyAnalysisLocators.QRY_DATE)
        self.inputDate(content)

    # 发电类型
    def inputSel_gc_type(self, index):
        # self.click(DistributedEnergyAnomalyAnalysisLocators.QRY_GC_TYPE)
        # locator = self.get_select_locator(
        #     DistributedEnergyAnomalyAnalysisLocators.QRY_GC_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        # self.click(DistributedEnergyAnomalyAnalysisLocators.QRY_ABSO_MODE)
        # locator = self.get_select_locator(
        #     DistributedEnergyAnomalyAnalysisLocators.QRY_ABSO_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        # self.click(DistributedEnergyAnomalyAnalysisLocators.BTN_SEARCH)
        self.btn_query()

# 高级应用→重点用户监测→分布式电源管理→分布式电源异常分析→分布式电源异常情况明细
class DistributedEnergyAnomalyDetailPage(Page):
    # 查询类型
    def inputChk_qry_type(self, index):
        self.clickRadioBox(index, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_query_date(self, content):
        # self.exec_script(DistributedEnergyAnomalyDetailLocators.DATE_JS)
        # self.input(content, *DistributedEnergyAnomalyDetailLocators.QRY_DATE)
        self.inputDate(content)

    # 异常类型
    def inputStr_except_type(self, index):
        # self.click(DistributedEnergyAnomalyDetailLocators.QRY_EXCEPT_TYPE)
        # locator = self.get_select_locator(
        #     DistributedEnergyAnomalyDetailLocators.QRY_EXCEPT_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 发电类型
    def inputSel_gc_type(self, index):
        # self.click(DistributedEnergyAnomalyDetailLocators.QRY_GC_TYPE)
        # locator = self.get_select_locator(
        #     DistributedEnergyAnomalyDetailLocators.QRY_GC_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        # self.click(DistributedEnergyAnomalyDetailLocators.QRY_ABSO_MODE)
        # locator = self.get_select_locator(
        #     DistributedEnergyAnomalyDetailLocators.QRY_ABSO_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询按钮
    def btn_search(self):
        # self.click(DistributedEnergyAnomalyDetailLocators.BTN_SEARCH)
        self.btn_query(True)
