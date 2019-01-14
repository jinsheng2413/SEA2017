# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterSuccessRateQuery_page.py
@time: 2018/10/10 14:48
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→抄表成功率查询（河北）
class MeterSuccessRateQueryPage(Page):
    # 按地区、厂家统计
    # 日期
    def inputDt_factory_date(self, content):
        self.inputDate(content)

    # 用户类型
    def inputSel_factory_cons_type(self, index):
        self.selectCheckBox(index)

    # 终端类型
    def inputSel_factory_tmnl_type(self, index):
        self.clean_label(index)
        self.selectCheckBox(index)

    # 通信方式
    def inputSel_comm_way(self, index):
        self.selectCheckBox(index)

    # 规约类型
    def inputSel_protocol_type(self, index):
        self.selectCheckBox(index)

    # 用户范围
    def inputSel_cons_range(self, index):
        self.selectDropDown(index)

    # 统计类型
    def inputSel_stat_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def factory_btn_search(self):
        self.btn_query()
