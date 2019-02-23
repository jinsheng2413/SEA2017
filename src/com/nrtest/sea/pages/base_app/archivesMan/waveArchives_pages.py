# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: waveArchives_pages.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→载波档案校正：载波台区统计
class WaveArchives_count_Page(Page):
    # 台区编号
    def inputStr_tg_no(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 统计分类
    def inputSel_stat_type(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 统计时间
    def inputDt_stat_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→档案管理→载波档案校正：载波用户明细
class WaveArchives_detail_Page(Page):
    # 台区编号
    def inputStr_tg_no(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 统计分类
    def inputSel_stat_type(self, name):
        self.selectDropDown(name, is_multi_elements=True, is_multi_tab=True)

    # 统计时间
    def inputDt_stat_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
