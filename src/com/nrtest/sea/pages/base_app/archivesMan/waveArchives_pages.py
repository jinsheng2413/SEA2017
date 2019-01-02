# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.waveArchives_Locators import WaveArchives_Locators


class WaveArchives_Page(Page):
    # 台区编号
    def inputStr_zone_no(self, value):
        self.input(value, *WaveArchives_Locators.QRY_ZONE_NO)

    # 台区名称
    def inputStr_zone_name(self, value):
        self.input(value, *WaveArchives_Locators.QRY_ZONE_NAME)

    # 统计分类
    def inputSel_countType(self, name):
        self.click(WaveArchives_Locators.QRY_COUNT_TYPE)
        locator = self.get_select_locator(
            WaveArchives_Locators.QRY_COUNT_TYPE_VALUE, name)
        self.click(locator)

    # 统计时间
    def inputStr_Count_time(self, value):
        self.input(value, *WaveArchives_Locators.QRY_COUNT_TIME)

    # 查询
    def btn_qry(self):
        self.click(WaveArchives_Locators.BTN_QRY)
