# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用--》费控管理--》本地费控--》电价参数管理

class EleParaMan_rate_Page(Page):



    # 开始时间
    def inputDT_startTimeOne(self, value):
        self.inputDate(value)  #, *EleParaManLocators.QRY_START_TIME_ONE)

    # 是否已生成参数
    def inputSel_ComeIntoPara_One(self, name):
        # self.click(EleParaManLocators.QRY_OR_COMEINTO_PARA_ONE)
        # locator = self.get_select_locator(
        #     EleParaManLocators.QRY_OR_COMEINTO_PARA_ONE, name)
        # self.click(locator)
        self.selectDropDown(name)


    # 结束时间
    def inputDT_EndTimeOne(self, value):
        self.inputDate(value, is_multi_tab=True)  # , *EleParaManLocators.QRY_END_TIME_ONE)

    # 费率来源
    def inputChk_fee_from(self, options):
        ls_option = options.replace(';', ',')
        self.clickCheckBox_g(ls_option)


        # 查询

    def btn_qry(self):
        # self.click(EleParaManLocators.BTN_QRY_ONE)
        self.btn_query(True)


class EleParaMan_step_Page(Page):
    # 开始时间
    def inputStr_startTimeTwo(self, value):
        self.inputDate(value)  # , *EleParaManLocators.QRY_START_TIME_ONE)
        # 是否已生成参数

    def inputSel_ComeIntoPara_Two(self, name):
        # self.click(EleParaManLocators.QRY_OR_COMEINTO_PARA_TWO)
        # locator = self.get_select_locator(
        #     EleParaManLocators.QRY_OR_COMEINTO_PARA_TWO, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 结束时间
    def inputStr_endTimeTwo(self, value):
        self.inputDate(value)  # , *EleParaManLocators.QRY_END_TIME_ONE)

    # 费率来源
    def inputChk_fee_from(self, options):
        # ls_option =options.split(',')
        # ls_option.pop()
        self.clickCheckBox_g('来源营销')

    def btn_qry(self):
        # self.click(EleParaManLocators.BTN_QRY_ONE)
        self.btn_query(True)
