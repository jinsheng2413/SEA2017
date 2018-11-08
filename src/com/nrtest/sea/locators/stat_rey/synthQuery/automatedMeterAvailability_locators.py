# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: automatedMeterAvailability_locators.py
@time: 2018/10/19 10:38
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→自动化抄表可用率
class AutomatedMeterAvailabilityLocators:
    # 全项采集成功率
    # 表计类型
    METER_TYPE = (By.XPATH, '//label[contains(text(),"表计类型")]/../div/div/img')
    # 表计类型→值
    METER_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')
    # 全项采集失败明细
    # 表计类型
    FAILED_METER_TYPE = (
        By.XPATH, '(//label[contains(text(),"表计类型")]/../div/div/img)[2]')
    # 表计类型→值
    FAILED_METER_TYPE_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端地址
    FAILED_TMNL_ADDR = (
        By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 查询日期
    FAILED_DATE = (
        By.XPATH, '(//label[contains(text(),"查询日期")]/../div/div/input)[2]')
    # 查询按钮
    FAILED_BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[5]')

    # 【JS属性】
    # 全项采集成功率→查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'
    # 全项采集失败明细→查询日期，删除readonly属性
    FAILED_DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
