# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossUnifiedView_locators.py
@time: 2018/11/1 13:42
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→台区线损统一视图→台区线损统一视图
class TgLineLossUnifiedViewLocators:
    # 台区编号
    QRY_TG_NO = (By.XPATH, '//label[contains(text(),"台区编号")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[1]')

    # 日线损
    # 查询日期，开始
    QRY_START_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询日期，结束
    QRY_END_DATE = (By.XPATH, '//label[contains(text(),"至")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH_DAY = (By.XPATH, '(//button[text()="查询"])[2]')

    # 月线损
    # 查询日期，开始
    QRY_START_DATE_TAB = (By.XPATH, '(//label[contains(text(),"查询日期")]/../div/div/input)[2]')
    # 查询日期，结束
    QRY_END_DATE_TAB = (By.XPATH, '(//label[contains(text(),"至")]/../div/div/input)[2]')
    # 查询按钮
    BTN_SEARCH_MONTH = (By.XPATH, '(//button[text()="查询"])[3]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[12].removeAttribute("readonly");'
    END_DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
    START_DATE_TAB_JS = 'document.getElementsByTagName("input")[26].removeAttribute("readonly");'
    END_DATE_TAB_JS = 'document.getElementsByTagName("input")[27].removeAttribute("readonly");'
