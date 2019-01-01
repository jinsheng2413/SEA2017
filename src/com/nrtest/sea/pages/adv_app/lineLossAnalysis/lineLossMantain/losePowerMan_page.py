# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: losePowerMan_page.py
@time: 2018/10/31 0031 13:27
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossMantain.losePowerMan_locators import LosePowerManLocators


# 高级应用-->线损分析--》线损模型维护--》线损模型设计
class LosePowerManPage(Page):
    # 考核单位状态
    def inputSel_assessUnitState(self, name):
        self.click(LosePowerManLocators.QRY_ASSESS_UNIT_STATE)
        locator = self.get_select_locator(
            LosePowerManLocators.QRY_ASSESS_UNIT_STATE_VALUE, name)
        print(locator)
        self.click(locator)

    # 组合标志
    def inputSel_CombinationSign(self, name):
        self.click(LosePowerManLocators.QRY_COMBINATION_SIGN)
        locator = self.get_select_locator(
            LosePowerManLocators.QRY_COMBINATION_SIGN_VALUE, name)
        self.click(locator)

    # 台区状态
    def inputSel_ZoneAreaState(self, name):
        self.click(LosePowerManLocators.QRY_ZONE_AREA_STATE)
        locator = self.get_select_locator(
            LosePowerManLocators.QRY_ZONE_AREA_STATE_VALUE, name)
        self.click(locator)

    # 考核单位名称
    def inputStr_assessUnitName(self, value):
        self.input(value, *LosePowerManLocators.QRY_ASSESS_UNIT_NAME)

    # 考核单位分类
    def inputSel_assessUnitClassfication(self, name):
        self.click(LosePowerManLocators.QRY_ASSESS_UNIT_CLASSFICATION)
        locator = self.get_select_locator(
            LosePowerManLocators.QRY_ASSESS_UNIT_CLASSFICATION_VALUE, name)
        print(locator)
        self.click(locator)

        # 查询

    def btn_qry(self):
        self.click(LosePowerManLocators.BTN_QRY)
