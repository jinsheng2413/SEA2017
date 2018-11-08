# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossAnalysis_locators.py
@time: 2018/10/30 15:52
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→线损统计分析→线路线损分析
class LineLossAnalysisLocators:
    # 线路编号
    QRY_LINE_NO = (By.XPATH, '//label[contains(text(),"线路编号")]/../div/input')
    # 线路名称
    QRY_LINE_NAME = (By.XPATH, '//label[contains(text(),"线路名称")]/../div/input')
    # 查询日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
