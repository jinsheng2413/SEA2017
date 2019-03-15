# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: distributedConsDataCurve_page.py
@time: 2019-03-15 09:38:57
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用 - 重点用户监测 - 分布式电源管理 - 分布式电源用户冻结曲线
class DistributedConsDataCurvePage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询类型
    def inputChk_query_type(self, value):
        self.clickRadioBox(value)

    # 日期
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 至
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # tab选择
    def inputChk_tab_name(self, value):
        self.clickTabPage(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
