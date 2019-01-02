# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkReduceManager_page.py
@time: 2018/11/16 0016 15:25
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.archivesVerficationMan.checkReduceManager_locators import \
    CheckReduceManagerLocators


# 系统管理--》档案核查管理--》考核减免管理
class CheckReduceManagerPage(Page):
    # 开始时间
    def inputStr_startTime(self, value):
        self.input(value, *CheckReduceManagerLocators.QRY_START_TIME)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *CheckReduceManagerLocators.QRY_END_TIME)

    # 申请单号
    def inputStr_applyNo(self, value):
        self.input(value, *CheckReduceManagerLocators.QRY_APPLY_NO)

    # 查询
    def btn_qry(self):
        self.click(CheckReduceManagerLocators.BTN_QRY)
