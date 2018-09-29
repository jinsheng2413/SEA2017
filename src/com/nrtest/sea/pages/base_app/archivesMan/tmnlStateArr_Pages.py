# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.tmnlStateArr_locators import TmnlStateArrLocators


class TmnlStateArrPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *TmnlStateArrLocators.QRY_TMNL_ADDR)

    # 终端状态
    def inputSel_tmnl_status(self, name):
        self.click(*TmnlStateArrLocators.QRY_TMNL_STATUS)
        locator = self.get_select_locator(TmnlStateArrLocators.QRY_TMNL_STATUS_VALUE, name)
        self.click(*locator)

    # 统计时间
    def inputStr_count_time(self, value):
        self.input(value, *TmnlStateArrLocators.QRY_COUNT_TIME)


    # 查询
    def btn_qry(self):
            self.click(*TmnlStateArrLocators.BTN_QRY)