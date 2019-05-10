# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: calculated_amount_page.py
@time: 2019/3/11 0011 16:15
@desc:
"""
from com.nrtest.common.base_page import Page


# 数据查询--计算量

class Calcluteamount_page(Page):
    # 时间方案
    def inputChk_time_blue_print(self, value):
        self.clickDt_Tab(value)
        # self.click_button(value)

    # 时间
    def inputDt_query_time(self, value):
        self.inputDate(value)

    # 电量计算单位
    def inputChk_ele_unit(self, value):
        self.clickRadioBox(value)

    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
