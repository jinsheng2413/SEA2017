# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlPowerCutEventQuery_locators.py
@time: 2018/11/5 10:02
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→终端停电事件查询
class TmnlPowerCutEventQueryLocators:
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 月份
    QRY_DATE = (By.XPATH, '//label[contains(text(),"月份")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 高级应用→配变监测分析→停电分析→终端停电事件查询→月终端停电明细
class TmnlPowerCutEventQueryMonthLocators:
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '(//label[contains(text(),"用户类型")]/../div/div/img)[2]')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 月份
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"月份")]/../div/div/input)[2]')
    # 停电次数
    QRY_POWER_CUT_TIME = (By.XPATH, '//label[contains(text(),"停电次数")]/../div/input')
    # 终端厂家
    QRY_TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    QRY_TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'


# 高级应用→配变监测分析→停电分析→终端停电事件查询→日终端停电明细
class TmnlPowerCutEventQueryDayLocators:
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '(//label[contains(text(),"用户类型")]/../div/div/img)[2]')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 停复电标识
    QRY_POWER_CUT_IDENTIFYING = (By.XPATH, '//label[contains(text(),"停复电标识")]/../div/div/img')
    QRY_POWER_CUT_IDENTIFYING_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端厂家
    QRY_TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    QRY_TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
