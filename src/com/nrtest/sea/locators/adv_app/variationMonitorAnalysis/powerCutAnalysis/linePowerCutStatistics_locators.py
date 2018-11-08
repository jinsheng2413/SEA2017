# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: linePowerCutStatistics_locators.py
@time: 2018/11/7 16:09
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→线路停电统计
class LinePowerCutStatisticsLocators:
    # 日期
    QRY_DATE = (By.XPATH, '//input[@name="startTimeField"]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'
