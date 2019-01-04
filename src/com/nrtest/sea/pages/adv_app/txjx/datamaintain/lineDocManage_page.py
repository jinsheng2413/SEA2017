# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用-->台线系统--》资料维护--》线路资料维护
class LineDocManagePage(Page):

    # 负责人
    def inputSel_master(self, name):
        # self.click(LineDataLocators.QRY_MASTER)
        # locator = self.get_select_locator(
        #     LineDataLocators.QRY_MASTER_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 线路名称
    def inputStr_lineName(self, value):
        self.input(value)  # , *LineDataLocators.QRY_LINE_NAME)

        # 查询

    def btn_qry(self):
        # self.click(LineDataLocators.BTN_QRY)
        self.btn_query()
