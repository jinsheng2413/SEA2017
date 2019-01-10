# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: runTmnlStatistics_page.py
@time: 2018/10/25 9:50
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→采集建设情况→运行终端统计
class RunTmnlStatisticsPage(Page):
    # 终端运行状态统计
    # 用户类型
    def inputSel_cons_type(self, index):
        # if index == 'c':
        #     self._find_element(RunTmnlStatisticsLocators.CONS_TYPE)
        # else:
        #     self.click(RunTmnlStatisticsLocators.CONS_TYPE)
        #     locator = self.get_select_locator(
        #         RunTmnlStatisticsLocators.CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(RunTmnlStatisticsLocators.CONS_TYPE)
        self.selectCheckBox(index)

    # 统计日期
    def inputDt_query_date(self, content):
        # self.exec_script(RunTmnlStatisticsLocators.DATE_JS)
        # self.input(content, *RunTmnlStatisticsLocators.DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(RunTmnlStatisticsLocators.BTN_SEARCH)
        self.btn_query()

    # 终端运行状态明细
    # 用户类型
    def inputSel_detail_cons_type(self, index):
        # if index == 'c':
        #     self._find_element(RunTmnlStatisticsLocators.DETAIL_CONS_TYPE)
        # else:
        #     self.click(RunTmnlStatisticsLocators.DETAIL_CONS_TYPE)
        #     locator = self.get_select_locator(
        #         RunTmnlStatisticsLocators.DETAIL_CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(RunTmnlStatisticsLocators.DETAIL_CONS_TYPE)
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 终端类型
    def inputSel_detail_tmnl_type(self, index):
        # if index == 'c':
        #     self._find_element(RunTmnlStatisticsLocators.DETAIL_TMNL_TYPE)
        # else:
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_TYPE)
        #     locator = self.get_select_locator(
        #         RunTmnlStatisticsLocators.DETAIL_TMNL_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_TYPE)
        self.selectCheckBox(index)

    # 通讯规约
    def inputSel_detail_tmnl_protocol(self, index):
        # if index == 'c':
        #     self._find_element(RunTmnlStatisticsLocators.DETAIL_TMNL_PROTOCOL)
        # else:
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_PROTOCOL)
        #     locator = self.get_select_locator(
        #         RunTmnlStatisticsLocators.DETAIL_TMNL_PROTOCOL_VALUE, index)
        #     self.click(locator)
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_PROTOCOL)
        self.selectCheckBox(index)

    # 通讯方式
    def inputSel_detail_tmnl_way(self, index):
        # if index == 'c':
        #     self._find_element(RunTmnlStatisticsLocators.DETAIL_TMNL_WAY)
        # else:
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_WAY)
        #     locator = self.get_select_locator(
        #         RunTmnlStatisticsLocators.DETAIL_TMNL_WAY_VALUE, index)
        #     self.click(locator)
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_WAY)
        self.selectCheckBox(index)

    # 终端厂家
    def inputSel_detail_tmnl_factory(self, index):
        # if index == 'c':
        #     self._find_element(RunTmnlStatisticsLocators.DETAIL_TMNL_FACTORY)
        # else:
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_FACTORY)
        #     locator = self.get_select_locator(
        #         RunTmnlStatisticsLocators.DETAIL_TMNL_FACTORY_VALUE, index)
        #     self.click(locator)
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_FACTORY)
        self.selectCheckBox(index)

    # 终端状态
    def inputSel_detail_tmnl_ststus(self, index):
        # if index == 'c':
        #     self._find_element(RunTmnlStatisticsLocators.DETAIL_TMNL_STATUS)
        # else:
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_STATUS)
        #     locator = self.get_select_locator(
        #         RunTmnlStatisticsLocators.DETAIL_TMNL_STATUS_VALUE, index)
        #     self.click(locator)
        #     self.click(RunTmnlStatisticsLocators.DETAIL_TMNL_STATUS)
        self.selectCheckBox(index)

    # 查询按钮
    def btn_detail_search(self):
        # self.click(RunTmnlStatisticsLocators.BTN_DETAIL_SEARCH)
        self.btn_query(True)
