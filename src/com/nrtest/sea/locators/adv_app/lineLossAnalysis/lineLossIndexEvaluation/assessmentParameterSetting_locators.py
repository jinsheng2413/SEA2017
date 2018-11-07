# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: assessmentParameterSetting_locators.py
@time: 2018/11/1 9:14
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→线损指标考核→考核参数设置
class AssessmentParameterSettingLocators:
    # 台区/线路名称
    QRY_TG_NAME = (
        By.XPATH, '//label[contains(text(),"台区/线路名称")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
