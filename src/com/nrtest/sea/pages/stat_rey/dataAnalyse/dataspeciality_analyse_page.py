# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: dataspeciality_analyse_page.py
@time: 2018/8/15 14:02
@desc:
"""
from com.nrtest.common.base_page import Page

DataSpecialityAnalyseLocators


class DataSpecialityAnalysePage(Page):
    # 点击唐山供电公司
    def spread_org_no(self):
        self.click(*DataSpecialityAnalyseLocators.SPREAD_ORG_NO)

    def tangshan_org_no(self):
        self.click(*DataSpecialityAnalyseLocators.TANGSHAN_ORG_NO)

    # 选择公变
    def select_cons_type(self):
        self.click(*DataSpecialityAnalyseLocators.SELECT_CONS_TYPE)

    def select_public(self):
        self.click(*DataSpecialityAnalyseLocators.SELECT_PUBLIC)

    # 时间
    def time(self):
        self.click(*DataSpecialityAnalyseLocators.TIME)

    def time_year1(self):
        self.click(*DataSpecialityAnalyseLocators.TIME_YEAR1)

    def time_year2(self):
        self.click(*DataSpecialityAnalyseLocators.TIME_YEAR2)

    # 开始时间-1月
    def time_mouth(self):
        self.click(*DataSpecialityAnalyseLocators.TIME_MOUTH)

    # 开始时间-确定
    def time_confirm(self):
        self.click(*DataSpecialityAnalyseLocators.TIME_CONFIRM)

    # 开始时间-13号
    def time_day(self):
        self.click(*DataSpecialityAnalyseLocators.TIME_DAY)

    # 查询
    def bin_search(self):
        self.click(*DataSpecialityAnalyseLocators.BTN_SEARCH)
