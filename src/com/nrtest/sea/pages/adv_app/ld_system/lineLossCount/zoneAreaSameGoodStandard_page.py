# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_zoneAreaSameGoodStandard.py
@time: 2019/1/28 0028 14:31
@desc:
"""
from com.nrtest.common.base_page import Page


class ZoneAreaSameGoodStandard_page(Page):
    # 选择人员
    def inputSel_select_person(self, value):
        self.selectDropDown(value)

    # 开始时间
    def inputDt_start_date(self, startDate):
        self.inputDate(startDate)

    # 结束时间
    def inputDt_end_date(self, end_Date):
        self.clean_label(end_Date)
        self.inputDate(end_Date)

    def btn_qry(self):
        self.btn_query()
