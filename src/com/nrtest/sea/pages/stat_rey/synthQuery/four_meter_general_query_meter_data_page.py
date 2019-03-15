# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: four_meter_general_query_meter_data_page.py
@time: 2019/3/15 17:13
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→多表合一综合查询:抄表数据
class FourMeterGeneralQueryMeterDataPage(Page):
    # 用户状态
    def inputSel_user_status(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # Tab页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
