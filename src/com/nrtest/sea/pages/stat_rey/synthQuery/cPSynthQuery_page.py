# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: cPSynthQuery_page.py
@time: 2018/10/20 14:04
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→采集点综合查询
class CPSynthQueryPage(Page):
    # 终端状态
    def inputSel_tmnl_status(self, index):
        self.selectDropDown(index)

    # 用户范围
    def inputSel_cons_range(self, index):
        self.selectDropDown(index)

    # 停电标志
    def inputSel_power_cut_flag(self, index):
        self.selectDropDown(index)

    # 终端投运日期
    def inputChk_tmnl_comm_date(self, index):
        self.clean_label(index)
        self.clickSingleCheckBox(index)

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 终端类型
    def inputChk_tmnl_type(self, value):
        self.clickRadioBox(value)

    # 接线方式
    def inputSel_wiring_mode(self, value):
        self.selectDropDown(value)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
