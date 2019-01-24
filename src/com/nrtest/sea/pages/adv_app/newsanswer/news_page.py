# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: news_page.py
@time: 2018-11-02 10:21
@desc:
"""

from com.nrtest.common.base_page import Page


class News_Page(Page):
    # 问题标题
    def inputStr_question_title(self, value):
        self.input(value)#, *News_Locators.QRY_QUESTION_TITLE)

    # 问题类型
    def inputSel_question_type(self, options):
        # self.click(News_Locators.QRY_QUESTION_TYPE)
        # locator = self.get_select_locator(
        #     News_Locators.QRY_QUESTION_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options)

    # 问题版块
    def inputSel_question_plate(self, options):
        # self.click(News_Locators.QRY_QUESTION_PLATE)
        # locator = self.get_select_locator(
        #     News_Locators.QRY_QUESTION_PLATE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options)

    # 紧急程度
    def inputSel_emergency_degree(self, options):
        # self.click(News_Locators.QRY_EMERGENCY_DEGREE)
        # locator = self.get_select_locator(
        #     News_Locators.QRY_EMERGENCY_DEGREE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options)

    # 查询方式
    def inputSel_query_type(self, options):
        # self.click(News_Locators.QRY_QUERY_TYPE)
        # locator = self.get_select_locator(
        #     News_Locators.QRY_QUERY_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options)

    # 问题状态
    def inputSel_question_status(self, options):
        # self.click(News_Locators.QRY_QUESTION_STATUS)
        # locator = self.get_select_locator(
        #     News_Locators.QRY_QUESTION_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options)

    # 开始日期
    def inputDt_start_date(self, value):
        self.input(value)#, *News_Locators.QRY_START_DATE)

    # 结束日期
    def inputDt_end_date(self, value):
        self.input(value)#, *News_Locators.QRY_END_DATE)

    # 查询
    def btn_qry(self):
        # self.click(News_Locators.BTN_QUERY)
        self.btn_query()
