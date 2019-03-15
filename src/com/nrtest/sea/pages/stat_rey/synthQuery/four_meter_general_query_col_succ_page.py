# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: four_meter_general_query_col_succ_page.py
@time: 2019/3/15 17:20
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→多表合一综合查询:采集成功率
class FourMeterGeneralQueryColSuccPage(Page):
    # 用户类型
    def inputSel_cons_sort(self, options):
        self.selectCheckBox(options)

    # 通信方式
    def inputSel_comm_mode(self, option):
        self.selectDropDown(option)

    # 终端厂家
    def inputSel_tmnl_factory(self, option):
        self.selectDropDown(option)

    # 芯片厂家
    def inputSel_chip_factory(self, option):
        self.selectDropDown(option)

    # 日期时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # Tab页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
