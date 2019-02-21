# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: runTmnlStatistics_page.py
@time: 2018/10/25 9:50
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→采集建设情况→运行设备统计→运行终端统计:终端运行状态统计
class RunTmnlStatisticsPage(Page):
    # 终端运行状态统计
    # 市、县直
    def inputChk_area_type(self, index):
        self.clickSingleCheckBox(index)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index)

    # 统计日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # Tab页选项
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 统计查询→采集建设情况→运行设备统计→运行终端统计:终端运行状态明细
class RunTmnlStatDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectCheckBox(index)

    # 通讯规约
    def inputSel_tmnl_protocol(self, index):
        self.selectCheckBox(index)

    # 通讯方式
    def inputSel_comm_mode(self, index):
        self.selectCheckBox(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectCheckBox(index)

    # 终端状态
    def inputSel_tmnl_status(self, index):
        self.selectCheckBox(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
