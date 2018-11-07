# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.costControlManage.eleParaMan_locators import EleParaManLocators


class EleParaManPage(Page):

    # 开始时间
    def inputStr_startTimeTwo(self, value):
        self.input(value, *EleParaManLocators.QRY_START_TIME_ONE)

    # 开始时间
    def inputStr_startTimeOne(self, value):
        self.input(value, *EleParaManLocators.QRY_START_TIME_ONE)

    # 是否已生成参数
    def inputSel_ComeIntoPara_One(self, name):
        self.click(*EleParaManLocators.QRY_OR_COMEINTO_PARA_ONE)
        locator = self.get_select_locator(
            EleParaManLocators.QRY_OR_COMEINTO_PARA_ONE, name)
        self.click(*locator)

        # 是否已生成参数

    def inputSel_ComeIntoPara_Two(self, name):
        self.click(*EleParaManLocators.QRY_OR_COMEINTO_PARA_TWO)
        locator = self.get_select_locator(
            EleParaManLocators.QRY_OR_COMEINTO_PARA_TWO, name)
        self.click(*locator)

    # 结束时间
    def inputStr_EndTimeOne(self, value):
        self.input(value, *EleParaManLocators.QRY_END_TIME_ONE)

    # 结束时间
    def inputStr_endTimeTwo(self, value):
        self.input(value, *EleParaManLocators.QRY_END_TIME_ONE)

        # 查询

    def btn_qryOne(self):
        self.click(*EleParaManLocators.BTN_QRY_ONE)

    # 查询
    def btn_qryTwo(self):
        self.click(*EleParaManLocators.BTN_QRY_TWO)
