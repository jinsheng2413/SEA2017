# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossStatisticsQuery_locators.py
@time: 2018/10/31 14:31
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→线损统计分析→线损统计查询
class LineLossStatisticsQueryLocators:
    # 线损分类
    QRY_LINE_LOSS_TYPE = (
        By.XPATH, '//label[contains(text(),"线损分类")]/../div/div/img')
    QRY_LINE_LOSS_TYPE_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 线损率
    QRY_LINE_LOSS_RATE = (
        By.XPATH, '//label[contains(text(),"线损率")]/../div/div/img')
    QRY_LINE_LOSS_RATE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    QRY_LINE_LOSS_RATE_INPUT = (
        By.XPATH, '//input[@class=" x-form-text x-form-field x-form-num-field "]')
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查")])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[12].removeAttribute("readonly");'
