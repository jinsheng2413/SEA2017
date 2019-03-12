# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: dataRey_locators.py
@time: 2019-03-12 09:32:46
@desc:
"""

from selenium.webdriver.common.by import By


class DataRey_locators:
    # 数据查询--电量数据查询
    BTN_SEARCH = (By.XPATH, '//*[@id="search_btn"]')

    # 数据查询--日冻结查询
    BTN_SEARCH2 = (By.XPATH, '//*[@id="searchBtn"]')

    # 数据管理--谣测值
    BTN_SEARCH3 = (By.XPATH, '//*[@id="search_btn"]')
