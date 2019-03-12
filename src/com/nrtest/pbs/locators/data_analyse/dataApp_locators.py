# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: dataApp_locators.py
@time: 2019-03-11 15:12:46
@desc:
"""

from selenium.webdriver.common.by import By


class DataApp_locators:
    # 数据分析--对端分析
    BTN_SEARCH = (By.XPATH, '//*[@id="searchBtn"]')
    # 数据分析--停电时间统计
    BTN_SEARCH1 = (By.XPATH, '//*[@id="search_btn"]')
