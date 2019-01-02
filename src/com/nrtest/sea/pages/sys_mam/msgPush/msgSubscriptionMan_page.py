# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: msgSubscriptionMan_page.py
@time: 2018/11/21 16:03
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→信息定制→推送信息定制→手机订阅→短信订阅管理
class MsgSubscriptionManPage(Page):
    # 订阅类型
    def inputSel_sub_type(self, option):
        # self.click(MsgSubscriptionManLocators.QRY_SUB_TYPE)
        # locator = self.get_select_locator(MsgSubscriptionManLocators.QRY_SUB_TYPE_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 发送范围
    def inputSel_send_scope(self, option):
        # self.click(MsgSubscriptionManLocators.QRY_SEND_SCOPE)
        # locator = self.get_select_locator(MsgSubscriptionManLocators.QRY_SEND_SCOPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(option)

    # 查询按钮
    def btn_search(self):
        # self.click(MsgSubscriptionManLocators.BTN_SEARCH)
        self.btn_query()
