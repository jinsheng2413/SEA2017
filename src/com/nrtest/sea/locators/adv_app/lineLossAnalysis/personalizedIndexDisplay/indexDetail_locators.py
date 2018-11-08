# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: indexDetail_locators.py
@time: 2018/11/2 14:55
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→同期线损→指标明细
class IndexDetailLocators:
    # 台区编号
    QRY_TG_NO = (By.XPATH, '//label[contains(text(),"台区编号")]/../div/input')
    # 台区名称
    QRY_TG_NAME = (By.XPATH, '//label[contains(text(),"台区名称")]/../div/input')
    # 时间选择
    QRY_DATE = (
        By.XPATH, '(//label[contains(text(),"时间选择")]/../div/div/input)[2]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 时间选择，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
