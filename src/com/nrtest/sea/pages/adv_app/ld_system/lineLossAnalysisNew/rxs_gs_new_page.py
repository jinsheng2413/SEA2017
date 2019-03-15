# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: rxs_gs_new_page.py
@time: 2019-03-14 15:38:08
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→线损统计(新)→台区日线损综合汇总报表(公司新)
class RxsGsNewPage(Page):

    def inputSel_org_no(self, index):
        self.selectDropDown(index)

    # 时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
