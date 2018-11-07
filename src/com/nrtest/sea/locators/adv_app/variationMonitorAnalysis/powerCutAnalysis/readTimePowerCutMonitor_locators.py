# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: readTimePowerCutMonitor_locators.py
@time: 2018/11/6 16:02
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→实时停电监测
class ReadTimePowerCutMonitorLocators:
    # 查询日期
    QRY_DATE = (By.XPATH, '(//input)[8]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'


# 高级应用→配变监测分析→停电分析→实时停电监测→实时停电明细
class ReadTimePowerCutDetailLocators:
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 信息推送
    QRY_INFORMATION_PUSH = (By.XPATH, '//label[contains(text(),"信息推送")]/../div/div/img')
    QRY_INFORMATION_PUSH_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
