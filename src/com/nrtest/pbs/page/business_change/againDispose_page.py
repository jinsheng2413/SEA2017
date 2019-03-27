# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: againDispose_page.py
@time: 2019-03-13 16:07
@desc:
"""
from com.nrtest.common.base_page import Page


# 业务变更→重处理
class AgainDisposePage(Page):
    # 处理方式
    def inputChk_dispose_type(self, value):
        self.clickRadioBox(value, number=True)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # Tab页名称
    def inputChk_tab_name(self, value):
        self.clickTabPage(value, is_by_js=True)

    # 提交按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
