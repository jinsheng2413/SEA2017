# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.eventRecResultStat_locators import \
    EventRecResultStatLocators


class EventRecResultStatPage(Page):
    # 开始时间
    def inputStr_start_timme(self, value):
        self.input(value, *EventRecResultStatLocators.QRY_START_TIME)

    # 事件类型
    def inputSel_event_type(self, name):
        self.click(*EventRecResultStatLocators.QRY_EVENT_TYPE)
        locator = self.get_select_locator(EventRecResultStatLocators.QRY_EVENT_TYPE_VALUE, name)
        self.click(*locator)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *EventRecResultStatLocators.QRY_END_TIME)

    # 查询
    def btn_qry(self):
        self.click(*EventRecResultStatLocators.BTN_QRY)
