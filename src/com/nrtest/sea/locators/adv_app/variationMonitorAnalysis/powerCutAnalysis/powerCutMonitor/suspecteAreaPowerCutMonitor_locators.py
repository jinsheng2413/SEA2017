# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: suspecteAreaPowerCutMonitor_locators.py
@time: 2018/11/6 13:39
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测
class SuspecteAreaPowerCutMonitorLocators:
    # 停电日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"停电日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 停电日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测→疑似停电线路查询
class SuspectePowerCutLineQueryLocators:
    # 是否恢复停电
    QRY_WHETHER_RECOVER_POWER_CUT = (By.XPATH, '//label[contains(text(),"是否恢复停电")]/../div/div/img')
    QRY_WHETHER_RECOVER_POWER_CUT_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 停电日期
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"停电日期")]/../div/div/input)[2]')
    # 停电时长
    QRY_POWER_CUT_START = (By.XPATH, '//label[contains(text(),"停电时长>=")]/../div/input')
    QRY_POWER_CUT_END = (By.XPATH, '//label[contains(text(),"停电时长<=")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 停电日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'


# 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测→疑似停电对象查询
class SuspectePowerCutObjectQueryLocators:
    # 是否线路停电
    QRY_WHETHER_LINE_POWER_CUT = (By.XPATH, '//label[contains(text(),"是否线路停电")]/../div/div/img')
    QRY_WHETHER_LINE_POWER_CUT_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 对象类型
    QRY_OBJECT_TYPE = (By.XPATH, '//label[contains(text(),"对象类型")]/../div/div/img')
    QRY_OBJECT_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 停电日期
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"停电日期")]/../div/div/input)[2]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 停电日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
