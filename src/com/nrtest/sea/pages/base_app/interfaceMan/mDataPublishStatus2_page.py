# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mDataPublishStatus2_page.py
@time: 2018-10-30 16:03
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.interfaceMan.mDataPublishStatus2_locators import MDataPublishStatus2_locators


class MDataPublishStatus2Page(Page):
    # 业务系统
    def inputSel_BusinessSystem(self, index):
        self.click(*MDataPublishStatus2_locators.QRY_BUSINESS_SYSTEM)
        locator = self.get_select_locator(MDataPublishStatus2_locators.QRY_BUSINESS_SYSTEM_VALUE, index)
        self.click(*locator)

    # 发布时间 开始
    def inputStr_receive_time(self, value):
        self.input(value, *MDataPublishStatus2_locators.QRY_DATE_BEGIN)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *MDataPublishStatus2_locators.QRY_DATE_END)

    # 查询
    def btn_qry(self):
        self.click(*MDataPublishStatus2_locators.BTN_QUERY)
