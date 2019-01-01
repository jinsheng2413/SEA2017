# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.curCollectSuccessRate_locators import \
    CurCollectSuccessRateLocators


# 基本应用→数据采集管理→采集质量分析→实时采集成功率
class CurCollectSuccessRatePage(Page):
    # 台区编号
    def inputStr_platformNo(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_PLATFORM_NO)
        self.input(value)

    # 台区名称
    def inputStr_platformName(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_PLATFORM_NAME)
        self.input(value)

    # 日期时间
    def inputStr_dateTime_detail(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_DATE_TIME_DETAIL)
        self.input(value)

    # 日期时间
    def inputStr_dateTime_count(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_DATE_TIME_COUNT)
        self.input(value)

    # 开始时间
    def inputStr_startTime(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_START_TIME)
        self.input(value)

    # 结束时间
    def inputStr_endTime(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_END_TIME)
        self.input(value)

    # 查询
    def btn_qry(self):
        self.click(CurCollectSuccessRateLocators.BTN_QRY)

    # 统计查询
    def btn_count_qry(self):
        self.click(CurCollectSuccessRateLocators.BTN_QRY_COUNT)

    # 明细查询
    def btn_detail_qry(self):
        self.click(CurCollectSuccessRateLocators.BTN_QRY_DETAIL)
