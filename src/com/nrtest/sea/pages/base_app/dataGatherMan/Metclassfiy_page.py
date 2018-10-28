# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.metclassfiy_locators import MetclassfiyLocators


class MetclassfiyPage(Page):
    # 模板名称
    def inputStr_templetName(self, value):
        self.input(value, *MetclassfiyLocators.QRY_TEMPLET_NAME)

    # 电能表类型
    def inputSel_meterType(self, name):
        self.click(*MetclassfiyLocators.QRY_METER_TYPE)
        locator = self.get_select_locator(MetclassfiyLocators.QRY_METER_TYPE_VALUE, name)
        self.click(*locator)

    # 操作
    def inputStr_perform(self, value):
        self.input(value, *MetclassfiyLocators.QRY_PERFORMER)

        # 查询

    def btn_qry(self):
        self.click(*MetclassfiyLocators.BTN_QRY)
