# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: historyPowerCutEventQuery_locators.py
@time: 2018/11/7 14:03
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→历史停电事件查询
class HistoryPowerCutEventQueryLocators:
    # 查询日期
    QRY_DATE = (By.XPATH, '(//input)[8]')
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 高级应用→配变监测分析→停电分析→历史停电事件查询→终端停电事件查询
class TmnlPowerCutEventQueryLocators:
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '(//label[contains(text(),"用户类型")]/../div/div/img)[2]')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端类型
    QRY_TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    QRY_TMNL_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '(//input)[22]')
    # 停复电标识
    QRY_POWER_CUT_IDENTIFYING = (By.XPATH, '//label[contains(text(),"停复电标识")]/../div/div/img')
    QRY_POWER_CUT_IDENTIFYING_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端厂家
    QRY_TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    QRY_TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 是否有效
    QRY_IS_VALID = (By.XPATH, '//label[contains(text(),"是否有效")]/../div/div/img')
    QRY_IS_VALID_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[21].removeAttribute("readonly");'


# 高级应用→配变监测分析→停电分析→历史停电事件查询→智能表停电事件查询
class IntelligentMeterPowerCutEventQueryLocators:
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '(//label[contains(text(),"用户类型")]/../div/div/img)[2]')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '//input[@id="hismpcdDateTimeField"]')
    # 事件正确性
    QRY_EVENT_CORRECTNESS = (By.XPATH, '//label[contains(text(),"事件正确性")]/../div/div/img')
    QRY_EVENT_CORRECTNESS_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 停电时长
    QRY_POWER_CUT_START = (By.XPATH, '//input[@id="hismeterCutFromTime"]')
    QRY_POWER_CUT_END = (By.XPATH, '//input[@id="hismeterCutToTime"]')
    # 电表厂家
    QRY_METER_FACTORY = (By.XPATH, '//label[contains(text(),"电表厂家")]/../div/div/img')
    QRY_METER_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 是否有效
    QRY_IS_VALID = (By.XPATH, '//label[contains(text(),"是否有效")]/../div/div/img')
    QRY_IS_VALID_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[20].removeAttribute("readonly");'
