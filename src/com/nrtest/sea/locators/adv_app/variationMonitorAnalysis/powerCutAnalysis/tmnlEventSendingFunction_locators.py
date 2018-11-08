# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlEventSendingFunction_locators.py
@time: 2018/11/7 15:26
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→终端是否具备停上电事件上送功能
class TmnlEventSendingFunctionLocators:
    # 查询日期
    QRY_DATE = (By.XPATH, '(//input)[7]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 高级应用→配变监测分析→停电分析→终端是否具备停上电事件上送功能→终端是否具备停上电事件上送功能明细
class TmnlEventSendingFunctionDeatilLocators:
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 终端类型
    QRY_TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    QRY_TMNL_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端厂家
    QRY_TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    QRY_TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端规约
    QRY_TMNL_PROTOCOL = (By.XPATH, '//label[contains(text(),"终端规约")]/../div/div/img')
    QRY_TMNL_PROTOCOL_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 是否具备停上电事件上送功能
    QRY_SENDING_FUNCTION = (By.XPATH, '//label[contains(text(),"是否具备停上电事件上送功能")]/../div/div/img')
    QRY_SENDING_FUNCTION_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
