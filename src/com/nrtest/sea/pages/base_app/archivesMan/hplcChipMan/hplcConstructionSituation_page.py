# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: hplc_chip_cover_detail_page.py
@time: 2019-04-11 14:14:05
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC芯片管理→hplc建设情况:HPLC芯片覆盖统计
class HplcChipCoverStatPage(Page):

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 基本应用→档案管理→HPLC芯片管理→hplc建设情况:HPLC芯片覆盖明细
class HplcChipCoverDetailPage(Page):
    # 设备类型
    def inputSel_equip_type(self, option):
        self.selectDropDown(option)

    # 是否覆盖
    def inputSel_is_corve(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→档案管理→HPLC芯片管理→hplc建设情况:HPLC芯片混装度统计
class HplcChipMixStatPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→档案管理→HPLC芯片管理→hplc建设情况:HPLC芯片混装度分析
class HplcChipMixAnalysePage(Page):
    # 是否混装
    def inputSel_is_max(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
