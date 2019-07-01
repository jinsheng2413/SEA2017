# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: checkResult_page.py
@time: 2019-07-01 10:08:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC管理→户变关系档案校核→户变关系校核结果
class CheckResultPage(Page):
    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)