# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: importantClientRealTimePowerCutMonitor_locators.py
@time: 2018/11/6 9:21
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→停电监测→重要客户实时停电监测→重要客户历史停电查询
class ImportantClientRealTimePowerCutMonitorLocators:
    # 电压等级
    QRY_VOLT_LEVEL = (
        By.XPATH, '(//label[contains(text(),"电压等级")]/../div/div/img)[2]')
    QRY_VOLT_LEVEL_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 停电开始日期
    QRY_START_DATE = (
        By.XPATH, '//label[contains(text(),"停电开始日期")]/../div/div/input')
    # 停电结束日期
    QRY_END_DATE = (
        By.XPATH, '//label[contains(text(),"停电结束日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 停电开始日期，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[18].removeAttribute("readonly");'
    # 停电结束日期，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[19].removeAttribute("readonly");'
