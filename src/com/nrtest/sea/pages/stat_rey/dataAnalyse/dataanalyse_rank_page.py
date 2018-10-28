# -*- coding:utf-8 -*-

'''
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: dataanalyse_rank_page.py
@time: 2018/8/8 13:44
@desc:
'''
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.dataAnalyse.dataanalyse_rank_locators import DataAnalyseRankLocators


class DataAnalyseRankPage(Page):
    # 点击供电单位
    def btn_org_no(self):
        self.click(*DataAnalyseRankLocators.ORG_NO)

    # 点击开始时间
    def btn_start_time(self):
        self.click(*DataAnalyseRankLocators.START_TIME)

    # 点击开始时间-2014年
    def btn_start_time_year1(self):
        self.click(*DataAnalyseRankLocators.START_TIME_YEAR1)

    def btn_start_time_year2(self):
        self.click(*DataAnalyseRankLocators.START_TIME_YEAR2)

    # 点击开始时间-1月
    def btn_start_time_mouth(self):
        self.click(*DataAnalyseRankLocators.START_TIME_MOUTH)

    # 点击开始时间-确定
    def btn_start_time_confirm(self):
        self.click(*DataAnalyseRankLocators.START_TIME_CONFIRM)

    # 点击开始时间-1号
    def btn_start_time_day(self):
        self.click(*DataAnalyseRankLocators.START_TIME_DAY)

    # 点击查询
    def btn_search(self):
        self.click(*DataAnalyseRankLocators.BTN_SEARCH)

    # 点击户号
    def btn_cons_no(self):
        self.click(*DataAnalyseRankLocators.BTN_CONS_NO)

    # 输入排名数量
    def inputStr_rank_num(self, value):
        self.input(value, *DataAnalyseRankLocators.RANK_NUM)

    # 用户类型
    def inputRSel_cons_type(self, index):
        self.click(*DataAnalyseRankLocators.DROP_DOWN)
        locator = self.get_select_locator(DataAnalyseRankLocators.CONS_TYPE_SPECIAL, index)
        self.click(*locator)
