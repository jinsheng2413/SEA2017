# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: loseCountPowerMan_page.py
@time: 2018/11/2 0002 8:57
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用-->线损分析--》线损模型维护--》线损计算模型管理
class LoseCountPowerManPage(Page):
    # 台区编码
    def inputStr_zoneAreaCode(self, value):
        # self.input(value, *LoseCountPowerManLocators.QRY_ZONE_AREA_CODE)

        self.input(value)

    # 台区运行状态
    def inputSel_zoneAreaRunStatus(self, name):
        # self.click(LoseCountPowerManLocators.QRY_ZONE_AREA_RUN_STATUS)
        # locator = self.get_select_locator(
        #     LoseCountPowerManLocators.QRY_ZONE_AREA_RUN_STATUS_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 台区名称
    def inputStr_zoneAreaName(self, value):
        # self.input(value, *LoseCountPowerManLocators.QRY_ZONE_NAME)
        self.input(value)

    # 责任人工号
    def inputStr_responsibilierNo(self, value):
        # self.input(value, *LoseCountPowerManLocators.QRY_RESPONSIBILITIER_NO)
        self.input(value)

        # 查询

    def btn_qry(self):
        # self.click(*LoseCountPowerManLocators.BTN_QRY)
        self.btn_query()
