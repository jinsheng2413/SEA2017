# -*- coding:utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysRunContrastQuery_locators.py
@time: 2018/11/6 15:24
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询--》报表管理--》国网报表--》采集系统运行指标
class SysRunContrastQueryLocators:
    # 【操作区】
    BTN_QRY = (By.XPATH,
               "//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
