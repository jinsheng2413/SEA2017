# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class StrategicArchivesMaintainPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)  # , *StrategicArchivesMaintainLocators.QRY_TMNLADDR)

    # 终端资产号
    def inputStr_TmnlNo(self, value):
        self.input(value)  # , *StrategicArchivesMaintainLocators.QRY_TMNLNO)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *StrategicArchivesMaintainLocators.QRY_USERNO)

        # 查询

    def btn_qry(self):
        # self.click(StrategicArchivesMaintainLocators.BTN_QRY)
        self.btn_query()
