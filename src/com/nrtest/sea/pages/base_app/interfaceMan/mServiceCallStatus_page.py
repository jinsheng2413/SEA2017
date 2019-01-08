# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mServiceCallStatus_page.py
@time: 2018-10-15 14:40
@desc:
"""

from com.nrtest.common.base_page import Page


class MServiceCallStatusPage(Page):
    # 业务系统
    def inputSel_business_system(self, value):
        self.selectDropDown(value)

    # 服务名称
    def inputSel_business_name(self, value):
        self.selectDropDown(value)

    # 调用时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
