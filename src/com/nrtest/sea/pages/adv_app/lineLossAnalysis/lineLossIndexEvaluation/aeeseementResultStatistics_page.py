# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: aeeseementResultStatistics_page.py
@time: 2018/11/1 10:18
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossIndexEvaluation.aeeseementResultStatistics_locators import \
    AeeseementResultStatisticsLocators


# 高级应用→线损分析→线损指标考核→考核结果统计
class AeeseementResultStatisticsPage(Page):
    # 责任人
    def inputSel_charge_person(self, index):
        self.click(*AeeseementResultStatisticsLocators.QRY_CHARGE_PERSON)
        locator = self.get_select_locator(
            AeeseementResultStatisticsLocators.QRY_CHARGE_PERSON_VALUE, index)
        self.click(*locator)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(AeeseementResultStatisticsLocators.DATE_JS)
        self.input(content, *AeeseementResultStatisticsLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*AeeseementResultStatisticsLocators.BTN_SEARCH)
