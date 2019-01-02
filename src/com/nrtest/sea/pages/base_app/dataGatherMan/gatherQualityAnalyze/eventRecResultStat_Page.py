# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class EventRecResultStatPage(Page):
    # 开始时间
    def inputStr_start_timme(self, content):
        # self.input(value, *EventRecResultStatLocators.QRY_START_TIME)
        self.inputDate(content)

    # 事件类型
    def inputSel_event_type(self, option):
        # self.click(EventRecResultStatLocators.QRY_EVENT_TYPE)
        # locator = self.get_select_locator(
        #     EventRecResultStatLocators.QRY_EVENT_TYPE_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 结束时间
    def inputStr_end_time(self, content):
        # self.input(value, *EventRecResultStatLocators.QRY_END_TIME)
        self.inputDate(content)

    # 查询
    def btn_qry(self):
        # self.click(EventRecResultStatLocators.BTN_QRY)
        self.btn_query()
