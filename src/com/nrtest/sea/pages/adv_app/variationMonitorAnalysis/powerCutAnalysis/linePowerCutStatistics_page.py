# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: linePowerCutStatistics_page.py
@time: 2018/11/7 16:13
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.linePowerCutStatistics_locators import \
    LinePowerCutStatisticsLocators


# 高级应用→配变监测分析→停电分析→线路停电统计
class LinePowerCutStatisticsPage(Page):
    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(LinePowerCutStatisticsLocators.DATE_JS)
        self.input(content, *LinePowerCutStatisticsLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*LinePowerCutStatisticsLocators.BTN_SEARCH)
