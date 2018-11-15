# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: databaseUpgradeStat_locators.py
@time: 2018/11/15 15:35
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→系统配置管理→数据库升级情况
class DatabaseUpgradeStatLocators:
    # 升级日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"升级日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 审核开始日期，删除readonly属性
    DATE_JS = 'document.getElementById("upGradeLogDate").removeAttribute("readonly");'
