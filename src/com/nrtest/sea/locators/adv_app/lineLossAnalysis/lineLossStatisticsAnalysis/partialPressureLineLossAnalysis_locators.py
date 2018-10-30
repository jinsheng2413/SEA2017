# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: partialPressureLineLossAnalysis_locators.py
@time: 2018/10/30 17:13
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→线损统计分析→分压线损分析
class PartialPressureLineLossAnalysisLocators:
    # 电压等级
    QRY_VOLTAGE_LEVEL = (By.XPATH, '//label[contains(text(),"电压等级")]/../div/div/input')
    QRY_VOLTAGE_LEVEL_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'
