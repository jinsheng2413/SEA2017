# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: aeeseementResultStatistics_locators.py
@time: 2018/11/1 9:57
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→线损指标考核→考核结果统计
class AeeseementResultStatisticsLocators:
    # 责任人
    QRY_CHARGE_PERSON = (
        By.XPATH, '//label[contains(text(),"责任人")]/../div/div/img')
    QRY_CHARGE_PERSON_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')