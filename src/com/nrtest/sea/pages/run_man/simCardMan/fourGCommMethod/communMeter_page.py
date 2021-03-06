# -*- coding:utf-8 -*-


"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: communMeter_page.py
@time: 2018/12/27 0009 9:43
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理-->SIM卡管理-->4G通信方式-->抄表情况
class CommumMeterPage(Page):

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options)

    # 终端运行状态
    def inputSel_tmnl_run_status(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
