# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: dataAmend_page.py
@time: 2019-07-08 11:07
@desc:
"""

from com.nrtest.common.base_page import Page


# 业务变更→数据修正:数据修正操作
class DataAmendPage(Page):
    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # Tab页名称
    def inputChk_tab_name(self, value):
        self.clickTabPage(value, is_by_js=True)

    # 缺相类型
    def inputChk_phase_type(self,value):
        self.clickRadioBox(value)

    # 提交按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
