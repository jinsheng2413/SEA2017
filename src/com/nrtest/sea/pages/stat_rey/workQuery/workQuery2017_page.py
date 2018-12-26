# -*- coding: utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: workQuery2017_page.py
@time: 2018/11/1 14:59
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.workQuery.workQuery2017_locators import WorkCount2017Locators, \
    WorkQuery2017Locators


# 统计查询→工单查询→工单查询2017
class WorkCount2017Page(Page):
    # 工单类型
    def inputSel_workTitle(self, options):
        # self.click(*WorkCount2017Locators.QRY_WORK_TITLE)
        # locator = self.get_select_locator(
        #     WorkCount2017Locators.QRY_WORK_TITLE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        #self.click(*WorkCount2017Locators.BTN_QRY)
        self.btn_query()


class WorkQuery2017Page(Page):
    # 工单编号
    def inputStr_workNo(self, value):
        self.input(value)#, *WorkQuery2017Locators.QRY_WORK_NO)

    # 工单处理人
    def inputStr_workMan(self, value):
        self.input(value)#, *WorkQuery2017Locators.QRY_WORK_MAN)

    # 工单类型
    def inputSel_workTitle(self, options):
        # self.click(*WorkQuery2017Locators.QRY_WORK_TITLE)
        # locator = self.get_select_locator(
        #     WorkQuery2017Locators.QRY_WORK_TITLE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(options)

    # 工单状态
    def inputSel_workStatus(self, options):
        # self.click(*WorkQuery2017Locators.QRY_WORK_STATUS)
        # locator = self.get_select_locator(
        #     WorkQuery2017Locators.QRY_WORK_STATUS_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(options)
    # 工单发生时间
    def inputStr_startDate(self, value):
        self.input(value)#, *WorkQuery2017Locators.QRY_STARTDATE)

    # 工单完成时间
    def inputStr_endDate(self, value):
        self.input(value)#, *WorkQuery2017Locators.QRY_ENDDATE)

    # 查询
    def btn_qry(self):
        #self.click(*WorkQuery2017Locators.BTN_QRY)
        self.btn_query()
