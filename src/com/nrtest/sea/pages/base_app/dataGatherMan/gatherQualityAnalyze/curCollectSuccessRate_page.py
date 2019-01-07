# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量分析→实时采集成功率
class CurCollectSuccessRatePage(Page):
    # 开始时间
    def inputDT_startTime(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_START_TIME)
        self.inputDate(value, True)

    # 结束时间
    def inputDT_endTime(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_END_TIME)
        self.inputDate(value, True)

    # 查询
    def btn_qry(self):
        # self.click(CurCollectSuccessRateLocators.BTN_QRY)
        self.btn_query(True)


class CurCollectSuccessRate_count_Page(Page):
    # 日期时间
    def inputDT_dateTime_count(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_DATE_TIME_COUNT)
        self.input(value)

    # 统计查询
    def btn_count_qry(self):
        # self.click(CurCollectSuccessRateLocators.BTN_QRY_COUNT)
        self.btn_query(True)


class CurCollectSuccessRate_detail_Page(Page):
    # 台区编号
    def inputStr_platformNo(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_PLATFORM_NO)
        self.input(value)

    # 台区名称
    def inputStr_platformName(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_PLATFORM_NAME)
        self.input(value)

        # 日期时间

    def inputDT_dateTime_detail(self, value):
        # self.input(value, *CurCollectSuccessRateLocators.QRY_DATE_TIME_DETAIL)
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
