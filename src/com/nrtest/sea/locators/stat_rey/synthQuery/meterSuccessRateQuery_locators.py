# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterSuccessRateQuery_locators.py
@time: 2018/10/10 14:20
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→抄表成功率查询（河北）
class MeterSuccessRateQueryLocators:
    # 按地区、厂家统计
    # 日期
    FACTORY_DATE = (
        By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 用户类型
    FACTORY_CONS_TYPE = (
        By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    # 用户类型→值
    FACTORY_CONS_TYPE_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端类型
    FACTORY_TMNL_TYPE = (
        By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    # 终端类型→值
    FACTORY_TMNL_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    FACTORY_BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')

    # 【JS属性】
    # 日期，删除readonly属性
    FACTORY_DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
