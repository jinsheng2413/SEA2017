# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mServiceCallStatus2_page.py
@time: 2018-10-31 9:05
@desc:
"""

from com.nrtest.common.base_page import Page


class MServiceCallStatus2Page(Page):
    # 业务系统
    def inputSel_business_system(self, value):
        self.selectDropDown(value)

    # 服务名称
    def inputSel_service_name(self, value):
        self.selectDropDown(value)

    # 调用时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 工单编号
    def inputStr_app_no(self, name):
        self.input(name)

    # 查询
    def btn_qry(self):
        self.btn_query()
