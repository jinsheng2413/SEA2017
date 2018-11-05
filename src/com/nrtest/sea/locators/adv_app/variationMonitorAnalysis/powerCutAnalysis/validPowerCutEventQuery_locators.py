# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: validPowerCutEventQuery_locators.py
@time: 2018/11/2 15:43
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→有效停电事件查询
class ValidPowerCutEventQueryLocators:
    # 有效停电事件查询
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '//input[@class=" x-form-text x-form-field  x-trigger-noedit"]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 高级应用→配变监测分析→停电分析→有效停电事件查询→有效停电明细
class ValidPowerCutDetailLocators:
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端类型
    QRY_TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    QRY_TMNL_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 当前是否停电
    QRY_WHETHER_POWER_CUT = (By.XPATH, '//label[contains(text(),"当前是否停电")]/../div/div/img')
    QRY_WHETHER_POWER_CUT_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 是否有效停电
    QRY_WHETHER_POWER_CUT_VALID = (By.XPATH, '//label[contains(text(),"是否有效停电")]/../div/div/img')
    QRY_WHETHER_POWER_CUT_VALID_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 是否补全
    QRY_COMPLEMENT = (By.XPATH, '//label[contains(text(),"是否补全")]/../div/div/img')
    QRY_COMPLEMENT_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端厂家
    QRY_TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    QRY_TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 停电时长
    QRY_POWER_CUT_START = (By.XPATH, '//input[@id="powerCutIntervalField_1"]')
    QRY_POWER_CUT_END = (By.XPATH, '//input[@id="powerCutIntervalField_2"]')
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
