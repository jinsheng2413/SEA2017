# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: indexAllocation_page.py
@time: 2018/11/2 14:15
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→同期线损→指标配置
class IndexAllocationPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content)

    # 台区状态
    def inputSel_tg_status(self, index):
        self.selectDropDown(index)

    # 责任人工号
    def inputStr_charge_person_no(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
