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
    # 日期
    def inputDt_date(self, content):
        # self.exec_script(SuccessRateTrendLocators.DATE_JS)
        # self.input(content, *SuccessRateTrendLocators.QRY_DATE)
        self.inputDate(content)

    # 本地通讯方式
    def inputSel_comm_mode(self, index):
        # self.click(SuccessRateTrendLocators.QRY_COMM_MODE)
        # locator = self.get_select_locator(
        #     SuccessRateTrendLocators.QRY_COMM_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 远程通讯方式
    def inputSel_coll_mode(self, index):
        # self.click(SuccessRateTrendLocators.QRY_COLL_MODE)
        # locator = self.get_select_locator(
        #     SuccessRateTrendLocators.QRY_COLL_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        # self.click(SuccessRateTrendLocators.QRY_ABSO_MODE)
        # locator = self.get_select_locator(
        #     SuccessRateTrendLocators.QRY_ABSO_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 发电类型
    def inputSel_elec_type(self, index):
        # self.click(SuccessRateTrendLocators.QRY_ELEC_TYPE)
        # locator = self.get_select_locator(
        #     SuccessRateTrendLocators.QRY_ELEC_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        # self.click(SuccessRateTrendLocators.BTN_SEARCH)
        self.btn_query()

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率统计
class SuccessRateStatisticsPage(Page):
    # 日期
    def inputDt_date(self, content):
        # self.exec_script(SuccessRateStatisticsLocators.DATE_JS)
        # self.input(content, *SuccessRateStatisticsLocators.QRY_DATE)
        self.inputDate(content)

    # 本地通讯方式
    def inputSel_comm_mode(self, index):
        # self.click(SuccessRateStatisticsLocators.QRY_COMM_MODE)
        # locator = self.get_select_locator(
        #     SuccessRateStatisticsLocators.QRY_COMM_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 远程通讯方式
    def inputSel_coll_mode(self, index):
        # self.click(SuccessRateStatisticsLocators.QRY_COLL_MODE)
        # locator = self.get_select_locator(
        #     SuccessRateStatisticsLocators.QRY_COLL_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        # self.click(SuccessRateStatisticsLocators.QRY_ABSO_MODE)
        # locator = self.get_select_locator(
        #     SuccessRateStatisticsLocators.QRY_ABSO_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 发电类型
    def inputSel_elec_type(self, index):
        # self.click(SuccessRateStatisticsLocators.QRY_ELEC_TYPE)
        # locator = self.get_select_locator(
        #     SuccessRateStatisticsLocators.QRY_ELEC_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        # self.click(SuccessRateStatisticsLocators.BTN_SEARCH)
        self.btn_query(True)

# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率明细
class SuccessRateDetailPage(Page):
    # 电能表用途
    def inputSel_meter_purpose(self, index):
        # self.click(SuccessRateDetailLocators.QRY_METER_PURPOSE)
        # locator = self.get_select_locator(
        #     SuccessRateDetailLocators.QRY_METER_PURPOSE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 发电类型
    def inputSel_elec_type(self, index):
        # self.click(SuccessRateDetailLocators.QRY_ELEC_TYPE)
        # locator = self.get_select_locator(
        #     SuccessRateDetailLocators.QRY_ELEC_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        # self.click(SuccessRateDetailLocators.QRY_ABSO_MODE)
        # locator = self.get_select_locator(
        #     SuccessRateDetailLocators.QRY_ABSO_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 日期
    def inputDt_date(self, content):
        # self.exec_script(SuccessRateDetailLocators.DATE_JS)
        # self.input(content, *SuccessRateDetailLocators.QRY_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(SuccessRateDetailLocators.BTN_SEARCH)
        self.btn_query(True)
