# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: terminalDataQuery_page.py
@time: 2018/8/13 0002 14:00
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→终端数据查询:基本档案
class TerminalDataQueryDocPage(Page):
    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 统计查询→综合查询→终端数据查询:数据展示
class TerminalDataQueryDataPage(Page):
    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # Tab页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 总加组
    def inputSel_added_group(self, option):
        self.selectDropDown(option)

    # 查询日期
    def inputStr_start_date(self, value):
        self.input(value)

    # 至
    def inputStr_end_date(self, value):
        self.input(value)

    # 父级查询
    def btn_search(self):
        self.btn_query(True)

    # 查询
    def btn_qry(self):
        self.btn_query(True, idx=2)
