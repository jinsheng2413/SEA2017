# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.collectSuccessRateStat_locators import \
    CollectSuccessRateStatLocators


class CollectSuccessRateStatPage(Page):
    # 查询时间
    def inputStr_checkDate(self, value):
        self.input(value, *CollectSuccessRateStatLocators.QRY_CHECK_DATE)

    # 查询
    def btn_qry(self):
        self.click(*CollectSuccessRateStatLocators.BTN_QRY)
