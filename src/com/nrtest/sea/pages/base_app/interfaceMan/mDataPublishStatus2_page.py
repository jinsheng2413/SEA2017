# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mDataPublishStatus2_page.py
@time: 2018-10-30 16:03
@desc:
"""

from com.nrtest.common.base_page import Page


class MDataPublishStatus2Page(Page):
    # 业务系统
    def inputSel_BusinessSystem(self, option):
        # self.click(MDataPublishStatus2_locators.QRY_BUSINESS_SYSTEM)
        # locator = self.get_select_locator(
        #     MDataPublishStatus2_locators.QRY_BUSINESS_SYSTEM_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 发布时间 开始
    def inputStr_receive_time(self, content):
        # self.input(value, *MDataPublishStatus2_locators.QRY_DATE_BEGIN)
        self.inputDate(content)

    # 结束时间
    def inputStr_end_time(self, content):
        # self.input(value, *MDataPublishStatus2_locators.QRY_DATE_END)
        self.inputDate(content)

    # 查询
    def btn_qry(self):
        # self.click(MDataPublishStatus2_locators.BTN_QUERY)
        self.btn_query()
