# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkReducePool_page.py
@time: 2018/11/20 0020 10:47
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.archivesVerficationMan.checkReducePool_locators import CheckReducePoolLocators


# 系统管理--》档案核查管理--》考核减免汇总
class CheckReducePoolPage(Page):
    # 申请单号
    def inputStr_applyNo(self, value):
        self.input(value, *CheckReducePoolLocators.QRY_APPLY_NO)

    # 工单状态
    def inputSel_workStatus(self, name):
        self.click(*CheckReducePoolLocators.QRY_WORK_STATUS)
        locator = self.get_select_locator(CheckReducePoolLocators.QRY_WORK_STATUS_VALUE, name)
        self.click(*locator)

    # 申请时间
    def inputStr_apply_time(self, value):
        self.input(value, *CheckReducePoolLocators.QRY_APPLY_DATE)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *CheckReducePoolLocators.QRY_APPLY_DATE_TO)

        # 查询

    def btn_qry(self):
        self.click(*CheckReducePoolLocators.BTN_QRY)
