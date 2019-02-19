# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: strategicArchivesQuery_page.py
@time: 2019-02-18 16:21:51
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→关口档案维护:厂站档案查询
class StrategicArchivesQuerySubPage(Page):
    # 直属
    def inputChk_directly(self, options):
        self.clickSingleCheckBox(options)

    # 厂站名称
    def inputStr_sub_station_name(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 基本应用→终端管理→关口档案维护:终端档案查询
class StrategicArchivesQueryTmnlPage(Page):
    # 直属
    def inputChk_directly(self, options):
        self.clickSingleCheckBox(options, is_multi_elements=True, is_multi_tab=True)

    # 电压等级
    def inputSel_volt_code(self, option):
        self.selectDropDown(option)

    # 采集点名称
    def inputStr_cp_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→终端管理→关口档案维护:电表档案查询
class StrategicArchivesQueryMeterPage(Page):
    # 直属
    def inputChk_directly(self, options):
        self.clickSingleCheckBox(options, is_multi_elements=True, is_multi_tab=True)

    # 电表厂家
    def inputSel_meter_factory(self, option):
        self.selectDropDown(option)

    # 规约类型
    def inputSel_protocol_type(self, option):
        self.selectDropDown(option)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)

    # 电表名称
    def inputStr_meter_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
