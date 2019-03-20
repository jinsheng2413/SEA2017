# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterRealTimePowerCutQuery_page.py
@time: 2018/11/6 15:18
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→配变监测分析→停电分析→表计实时停上电信息查询
class MeterRealTimePowerCutQueryPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 电表资产号
    def inputStr_meter_asset_no(self, content):
        self.input(content)

    # 停电标志
    def inputSel_power_cut_flag(self, index):
        self.selectDropDown(index)

    # 查询类型
    def inputChk_qry_date_type(self, index):
        self.clickRadioBox(index)

    # 开始日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(idx=2)
