# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: msgSendQuery_page.py
@time: 2018/11/22 13:56
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.msgPush.msgSendQuery_locators import MsgSendQueryLocators


# 系统管理→信息定制→推送信息定制→手机订阅→短信发送查询
class MsgSendQueryPage(Page):
    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content, *MsgSendQueryLocators.QRY_CONS_NO)

    # 开始时间
    def inputDt_start_date(self, content):
        self.exec_script(MsgSendQueryLocators.START_DATE_JS)
        self.input(content, *MsgSendQueryLocators.QRY_START_DATE)

    # 结束时间
    def inputDt_end_date(self, content):
        self.exec_script(MsgSendQueryLocators.END_DATE_JS)
        self.input(content, *MsgSendQueryLocators.QRY_END_DATE)

    # 发送状态
    def inputSel_send_stat(self, index):
        if index == 'c':
            self._find_element(*MsgSendQueryLocators.QRY_SEND_STAT)
        else:
            self.click(*MsgSendQueryLocators.QRY_SEND_STAT)
            locator = self.get_select_locator(
                MsgSendQueryLocators.QRY_SEND_STAT_VALUE, index)
            self.click(*locator)
            self.click(*MsgSendQueryLocators.QRY_SEND_STAT)

    # 发送方式
    def inputSel_send_way(self, index):
        if index == 'c':
            self._find_element(*MsgSendQueryLocators.QRY_SEND_WAY)
        else:
            self.click(*MsgSendQueryLocators.QRY_SEND_WAY)
            locator = self.get_select_locator(
                MsgSendQueryLocators.QRY_SEND_WAY_VALUE, index)
            self.click(*locator)
            self.click(*MsgSendQueryLocators.QRY_SEND_WAY)

    # 发送人
    def inputStr_send_man(self, content):
        self.input(content, *MsgSendQueryLocators.QRY_SEND_MAN)

    # 查询按钮
    def btn_search(self):
        self.click(*MsgSendQueryLocators.BTN_SEARCH)
