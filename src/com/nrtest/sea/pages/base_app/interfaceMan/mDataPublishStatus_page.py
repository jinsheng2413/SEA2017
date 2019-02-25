# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mDataPublishStatus_page.py
@time: 2018-09-21 9:42
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.interfaceMan.mDataPublishStatus import MDataPublishStatus_locators


class MDataPublishStatusPage(Page):

    # 业务系统
    def inputSel_BusinessSystem(self, option):
        self.selectDropDown(option)

    # 发布时间 开始
    def inputDt_receive_time(self, value):
        self.input(value, *MDataPublishStatus_locators.QRY_DATE_BEGIN)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
