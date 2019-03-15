# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: balanceBrowse_locators.py
@time: 2019-03-15 10:01
@desc:
"""

from selenium.webdriver.common.by import By


# 线损分析→母平浏览:母平汇总
class BalanceBrowseCollectLocators:
    # 查询按钮
    BTN_QRY = (By.XPATH, '//*[@id="search_btn"]')


# 线损分析→母平浏览:母平查询
class BalanceBrowseQueryLocators:
    # 查询按钮
    BTN_QRY = (By.XPATH, '//*[@id="searchBtn"]')
