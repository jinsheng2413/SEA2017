# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class ArchivesAutoReviewPage(Page):

    # 导入电表信息
    def inputSel_leadInto_meter_info(self, name):
        # self.click(ArchivesAutoReviewLocators.QRY_LEADINTO_METER_INFO)
        # locator = self.get_select_locator(
        #     ArchivesAutoReviewLocators.QRY__LEADINTO_METER_INFO_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 时间
    def inputStr_date(self, value):
        self.inputDate(value)  # , *ArchivesAutoReviewLocators.QRY_DATE)

    # 查询
    def btn_qry(self):
        # self.click(ArchivesAutoReviewLocators.BTN_QRY)
        self.btn_query()
