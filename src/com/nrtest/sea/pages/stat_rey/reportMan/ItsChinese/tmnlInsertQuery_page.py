# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: tmnlInsertQuery_page.py
@time: 2018/11/7 0007 14:59
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.reportMan.ItsChinese.tmnlInsertQuery_locators import TmnlInsertQueryLocators


# 统计查询-->报表管理-->国网报表-->智能电能表及终端设备接入情况
class TmnlInsertQueryPage(Page):
    # 终端厂家
    def inputSel_tmnlFactory(self, name):
        self.click(*TmnlInsertQueryLocators.QRY_TMNL_FACTORY)
        locator = self.get_select_locator(TmnlInsertQueryLocators.QRY_TMNL_FACTORY_VALUE, name)
        self.click(*locator)

    # 统计口径
    def inputSel_countCaliber(self, name):
        self.click(*TmnlInsertQueryLocators.QRY_COUNT_CALIBER)
        locator = self.get_select_locator(TmnlInsertQueryLocators.QRY_COUNT_CALIBER_VALUE, name)
        self.click(*locator)


    # 终端类型
    def inputSel_tmnlType(self, name):
        self.click(*TmnlInsertQueryLocators.QRY_TMNL_TYPE)
        locator = self.get_select_locator(TmnlInsertQueryLocators.QRY_TMNL_TYPE_VALUE, name)
        self.click(*locator)


    # 接收时间
    def inputStr_date(self, value):
        self.input(value, *TmnlInsertQueryLocators.QRY_DATE)

    # 结束时间
    def inputStr_to(self, value):
        self.input(value, *TmnlInsertQueryLocators.QRY_TO)

    # 查询
    def btn_qry(self):
            self.click(*TmnlInsertQueryLocators.BTN_QRY)