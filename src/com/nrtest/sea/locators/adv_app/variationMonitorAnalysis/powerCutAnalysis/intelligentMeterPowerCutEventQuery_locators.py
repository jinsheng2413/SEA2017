# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: intelligentMeterPowerCutEventQuery_locators.py
@time: 2018/11/5 14:24
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→智能表停电事件查询
class IntelligentMeterPowerCutEventQueryLocators:
    # 用户类型
    QRY_CONS_TYPE = (
        By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    QRY_CONS_TYPE_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '(//input)[9]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 高级应用→配变监测分析→停电分析→智能表停电事件查询→智能表停电明细
class IntelligentMeterPowerCutEventQueryDetailLocators:
    # 用户类型
    QRY_CONS_TYPE = (
        By.XPATH, '(//label[contains(text(),"用户类型")]/../div/div/img)[2]')
    QRY_CONS_TYPE_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 日期
    QRY_DATE = (By.XPATH, '//input[@id="mpcdDateTimeField"]')
    # 事件正确性
    QRY_EVENT_CORRECTNESS = (
        By.XPATH, '//label[contains(text(),"事件正确性")]/../div/div/img')
    QRY_EVENT_CORRECTNESS_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 停电时长
    QRY_POWER_CUT_START = (By.XPATH, '//input[@id="meterCutFromTime"]')
    QRY_POWER_CUT_END = (By.XPATH, '//input[@id="meterCutToTime"]')
    # 电表厂家
    QRY_METER_FACTORY = (
        By.XPATH, '//label[contains(text(),"电表厂家")]/../div/div/img')
    QRY_METER_FACTORY_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[16].removeAttribute("readonly");'
