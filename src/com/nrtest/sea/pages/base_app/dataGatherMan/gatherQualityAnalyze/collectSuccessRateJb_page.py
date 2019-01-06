# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class CollectSuccessRateJbPage(Page):
    # 通信规约
    def inputSel_conmunicationGlue(self, name):
        # self.click(CollectSuccessRateJbLocators.QRY_COMUNICATION_GLUE)
        # locator = self.get_select_locator(
        # CollectSuccessRateJbLocators.QRY_COMUNICATION_GLUE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 终端厂家
    def inputSel_TmnlFactory(self, name):
        # self.click(CollectSuccessRateJbLocators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(
        # CollectSuccessRateJbLocators.QRY_TMNL_FACTORY_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 相位
    def inputSel_phase(self, name):
        # self.click(CollectSuccessRateJbLocators.QRY_PHASE)
        # locator = self.get_select_locator(
        # CollectSuccessRateJbLocators.QRY_PHASE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 通信方式
    def inputSel_conmunicationMode(self, name):
        # self.click(CollectSuccessRateJbLocators.QRY_COMUNICATION_MODE)
        # locator = self.get_select_locator(
        #     CollectSuccessRateJbLocators.QRY_COMUNICATION_MODE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 用户类型
    def inputSel_user_type(self, name):
        # self.click(CollectSuccessRateJbLocators.QRY_USER_TYPE)
        # locator = self.get_select_locator(
        #     CollectSuccessRateJbLocators.QRY_USER_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    #
    ## 芯片厂家
    def inputSel_pieceFactory(self, name):
        # self.click(CollectSuccessRateJbLocators.QRY_PIECE_FACTORY)
        # locator = self.get_select_locator(
        #     CollectSuccessRateJbLocators.QRY_PIECE_FACTORY_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 日期时间
    def inputStr_date(self, value):
        # self.input(value, *CollectSuccessRateJbLocators.QRY_DATE_TIME)
        # self.input(value)
        self.inputDate(value)

    ## 通信类型
    def inputSel_conmunicationtype(self, name):
        # self.click(CollectSuccessRateJbLocators.QRY_CONMUNICATION_TYPE)
        # locator = self.get_select_locator(
        #     CollectSuccessRateJbLocators.QRY_CONMUNICATION_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 查询
    def btn_qry(self):
        # self.click(CollectSuccessRateJbLocators.BTN_QRY)
        self.btn_query()
