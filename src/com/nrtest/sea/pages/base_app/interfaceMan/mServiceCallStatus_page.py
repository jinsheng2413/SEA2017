# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mServiceCallStatus_page.py
@time: 2018-10-15 14:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→接口管理→其他业务接口→服务调用情况:服务调用统计
class MServiceCallStatusPage(Page):

    # 业务系统
    def inputSel_business_system(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 服务名称
    def inputSel_service_name(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 调用时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.curr_click(btn_name='统计')


# 基本应用→接口管理→其他业务接口→服务调用情况:服务调用明细
class MServiceCallStatus_detail_Page(Page):

    # 业务系统
    def inputSel_business_system(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 服务名称
    def inputSel_service_name(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

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
