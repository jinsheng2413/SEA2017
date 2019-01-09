# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class WaveArchives_Page(Page):
    # 台区编号
    def inputStr_zone_no(self, value):
        self.input(value)

    # 台区名称
    def inputStr_zone_name(self, value):
        self.input(value)

    # 统计分类
    def inputSel_count_type(self, name):
        self.selectDropDown(name)

    # 统计时间
    def inputDt_count_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
