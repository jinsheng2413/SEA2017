# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: hplc_gather_integrity_rate_page.py
@time: 2019-04-24 16:26:18
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC管理→户变关系档案校核→台户异常处理情况
class HplcGatherIntegrityRatePage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 数据来源
    def inputChk_data_src(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
