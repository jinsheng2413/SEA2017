# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class ArchivesChangeRecordPage(Page):
    # 设备类型
    def inputSel_device_type(self, name):
        # self.click(ArchivesChangeRecordLocators.QRY_DEVICE_TYPE)
        # locator = self.get_select_locator(
        #     ArchivesChangeRecordLocators.QRY_DEVICE_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 变更类型
    def inputSel_change_type(self, name):
        # self.click(ArchivesChangeRecordLocators.QRY_CHANGE_TYPE)
        # locator = self.get_select_locator(
        #     ArchivesChangeRecordLocators.QRY_CHANGE_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 接收时间
    def inputDt_start_time(self, value):
        # self.input(value, *ArchivesChangeRecordLocators.QRY_START_TIME)
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        # self.input(value, *ArchivesChangeRecordLocators.QRY_END_TIME)
        self.inputDate(value)

    def inputChk_cons_type(self, option):
        # self.click(ArchivesChangeRecordLocators.BTN_SPECIAL_CHANGE)
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        # self.click(ArchivesChangeRecordLocators.BTN_QRY)
        self.btn_query()
