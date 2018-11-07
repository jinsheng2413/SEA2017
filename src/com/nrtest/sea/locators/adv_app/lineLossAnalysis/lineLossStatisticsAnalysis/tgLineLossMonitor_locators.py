# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossMonitor_locators.py
@time: 2018/10/31 15:44
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→线损统计分析→台区线损监测
class TgLineLossMonitorLocators:
    # 指标类型
    QRY_POINTER_TYPE = (By.XPATH, '//label[contains(text(),"指标类型")]/../div/div/img')
    QRY_POINTER_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'
