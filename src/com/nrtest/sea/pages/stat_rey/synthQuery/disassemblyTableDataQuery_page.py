# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: disassemblyTableDataQuery_page.py
@time: 2018/10/9 14:01
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.disassemblyTableDataQuery_locators import \
    DisassemblyTableDataQueryLocators

# 统计查询→综合查询→销户和拆表数据查询
class DisassemblyTableDataQueryPage(Page):
    # 用户名称
    def inputStr_cons_name(self, content):
        self.input(content)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 电能表资产号
    def inputStr_meter_asset_no(self, content):
        self.input(content)

    # 开始时间
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束时间
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

    # 选择指定行
    def inputRow_select_row(self, row_item):
        self.select_row(row_item)

    # TAB页名称
    def inputChk_tab_name(self, tabName):
        self.clickTabPage(tabName)

    # TAB页开始日期
    def inputDt_tab_start_date(self, content):
        self.inputDate(content)

    # TAB页结束日期
    def inputDt_tab_end_date(self, content):
        self.inputDate(content)

    # 曲线类型
    def inputSel_curve_type(self, content):
        self.specialDropdown(content, DisassemblyTableDataQueryLocators.CURVE_TYPE)

    # TAB页查询按钮
    def btn_qry(self):
        self.btn_query(True, idx=2)
