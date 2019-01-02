# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: runMeterStatistics_page.py
@time: 2018/10/25 15:08
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→采集建设情况→运行电能表统计
class RunMeterStatisticsPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        # if index == 'c':
        #     self._find_element(RunMeterStatisticsLocators.CONS_TYPE)
        # else:
        #     self.click(RunMeterStatisticsLocators.CONS_TYPE)
        #     locator = self.get_select_locator(
        #         RunMeterStatisticsLocators.CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(RunMeterStatisticsLocators.CONS_TYPE)
        self.selectCheckBox(index)

    # 统计日期
    def inputDt_date(self, content):
        # self.exec_script(RunMeterStatisticsLocators.DATE_JS)
        # self.input(content, *RunMeterStatisticsLocators.DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(RunMeterStatisticsLocators.BTN_SEARCH)
        self.btn_query()

    # 终端运行状态明细
    # 用户类型
    def inputSel_detail_cons_type(self, index):
        # if index == 'c':
        #     self._find_element(RunMeterStatisticsLocators.DETAIL_CONS_TYPE)
        # else:
        #     self.click(RunMeterStatisticsLocators.DETAIL_CONS_TYPE)
        #     locator = self.get_select_locator(
        #         RunMeterStatisticsLocators.DETAIL_CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(RunMeterStatisticsLocators.DETAIL_CONS_TYPE)
        self.selectCheckBox(index, is_multi_elements=True, is_multi_tab=True)

    # 通信方式
    def inputSel_detail_tmnl_way(self, index):
        # if index == 'c':
        #     self._find_element(RunMeterStatisticsLocators.DETAIL_TMNL_WAY)
        # else:
        #     self.click(RunMeterStatisticsLocators.DETAIL_TMNL_WAY)
        #     locator = self.get_select_locator(
        #         RunMeterStatisticsLocators.DETAIL_TMNL_WAY_VALUE, index)
        #     self.click(locator)
        #     self.click(RunMeterStatisticsLocators.DETAIL_TMNL_WAY)
        self.selectCheckBox(index)

    # 通讯规约
    def inputSel_detail_tmnl_protocol(self, index):
        # if index == 'c':
        #     self._find_element(RunMeterStatisticsLocators.DETAIL_TMNL_PROTOCOL)
        # else:
        #     self.click(RunMeterStatisticsLocators.DETAIL_TMNL_PROTOCOL)
        #     locator = self.get_select_locator(
        #         RunMeterStatisticsLocators.DETAIL_TMNL_PROTOCOL_VALUE, index)
        #     self.click(locator)
        #     self.click(RunMeterStatisticsLocators.DETAIL_TMNL_PROTOCOL)
        self.selectCheckBox(index)

    # 设备类型
    def inputSel_detail_device_type(self, index):
        # if index == 'c':
        #     self._find_element(RunMeterStatisticsLocators.DETAIL_DEVICE_TYPE)
        # else:
        #     self.click(RunMeterStatisticsLocators.DETAIL_DEVICE_TYPE)
        #     locator = self.get_select_locator(
        #         RunMeterStatisticsLocators.DETAIL_DEVICE_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(RunMeterStatisticsLocators.DETAIL_DEVICE_TYPE)
        self.selectCheckBox(index)

    # 电能表厂家
    def inputSel_detail_meter_factory(self, index):
        # if index == 'c':
        #     self._find_element(RunMeterStatisticsLocators.DETAIL_METER_FACTORY)
        # else:
        #     self.click(RunMeterStatisticsLocators.DETAIL_METER_FACTORY)
        #     locator = self.get_select_locator(
        #         RunMeterStatisticsLocators.DETAIL_METER_FACTORY_VALUE, index)
        #     self.click(locator)
        #     self.click(RunMeterStatisticsLocators.DETAIL_METER_FACTORY)
        self.selectCheckBox(index)

    # 电能表状态
    def inputSel_detail_meter_ststus(self, index):
        # if index == 'c':
        #     self._find_element(RunMeterStatisticsLocators.DETAIL_METER_STATUS)
        # else:
        #     self.click(RunMeterStatisticsLocators.DETAIL_METER_STATUS)
        #     locator = self.get_select_locator(
        #         RunMeterStatisticsLocators.DETAIL_METER_STATUS_VALUE, index)
        #     self.click(locator)
        #     self.click(RunMeterStatisticsLocators.DETAIL_METER_STATUS)
        self.selectCheckBox(index)

    # 查询按钮
    def btn_detail_search(self):
        # self.click(RunMeterStatisticsLocators.BTN_DETAIL_SEARCH)
        self.btn_query(True)
