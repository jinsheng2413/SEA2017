# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.txjx.datamaintain.checkpointdata_locators import CheckpointdataLocators


# 高级应用-->台线系统--》资料维护--》线路考核点资料维护
class CheckpointdataPage(Page):
    # 用户编号
    def inputStr_userNo(self, value):
        self.input(value, *CheckpointdataLocators.QRY_USER_NO)

    # 电表正反向
    def inputSel_meterFr(self, name):
        self.click(CheckpointdataLocators.QRY_METER_FR)
        locator = self.get_select_locator(
            CheckpointdataLocators.QRY_METER_FR_VALUE, name)
        self.click(locator)

    # 用户名称
    def inputStr_userName(self, value):
        self.input(value, *CheckpointdataLocators.QRY_USER_NAME)

    # 查询

    def btn_qry(self):
        self.click(CheckpointdataLocators.BTN_QRY)
