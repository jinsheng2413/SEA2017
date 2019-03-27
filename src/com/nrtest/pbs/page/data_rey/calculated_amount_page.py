# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_calculated_amount.py
@time: 2019/3/11 0011 16:15
@desc:
"""
from com.nrtest.pbs.tree.tree_page import TreePBSPage


# 数据查询--计算量

class Calcluteamount_page(TreePBSPage):
    # 时间方案
    def inputBtn_time_blue_print(self, value):
        self.click_button(value)

    # 时间
    def inputDt_query_time(self, value):
        self.inputDate(value)

    # 电量计算单位
    def inputChk_ele_unit(self, value):
        self.clickRadioBox(value, name=True)

    def btn_qry(self, value):
        self.btn_query(is_multi_tab=True)
