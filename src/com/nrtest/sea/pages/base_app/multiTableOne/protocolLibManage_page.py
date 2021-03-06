# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: protocolLibManage_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→多表合→协议库管理

class ProtocolLibManageLocatorsPage(Page):
    # 协议名称
    def inputStr_protocol_name(self, value):
        self.input(value)

    # 厂商名称
    def inputStr_manufacturer_name(self, value):
        self.input(value)

    # 协议类型
    def inputStr_protocol_type(self, value):
        self.input(value)

    # 表记类型
    def inputStr_meter_type(self, value):
        self.input(value)

    # 维护时间
    def inputDt_maintenance_time(self, value):
        self.inputDate(value)

    # 到
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 有效标志
    def inputSel_effective_sign(self, name):
        self.selectDropDown(name)

    # 协议版本号
    def inputStr_protocol_version_no(self, value):
        self.input(value)

    # 协议代码
    def inputStr_protocol_code(self, value):
        self.input(value)

    # 查询方式
    def inputChk_query_type(self, value):
        self.clickRadioBox(value)


    # 查询
    def btn_qry(self):
        self.btn_query()
