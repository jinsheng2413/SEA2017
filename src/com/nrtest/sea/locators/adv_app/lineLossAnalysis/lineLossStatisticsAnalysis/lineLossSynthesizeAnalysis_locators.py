# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossSynthesizeAnalysis_locators.py
@time: 2018/10/31 11:37
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→线损统计分析→线损综合分析
class LineLossSynthesizeAnalysisLocators:
    # 线损类别
    QRY_LINE_LOSS_TYPE = (By.XPATH, '//label[contains(text(),"线损类别")]/../div/div/input')
    QRY_LINE_LOSS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
