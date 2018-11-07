# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossAbnormalReport_locators.py
@time: 2018/11/2 11:00
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→台区线损统计查询→台区线损异常报表
class TgLineLossAbnormalReportLocators:
    # 线损维度
    QRY_LINE_LOSS_DIMENSION = (
        By.XPATH, '//label[contains(text(),"线损维度")]/../div/div/img')
    QRY_LINE_LOSS_DIMENSION_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 统计周期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"统计周期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
