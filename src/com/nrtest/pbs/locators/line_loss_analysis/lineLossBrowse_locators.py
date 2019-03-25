# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossBrowse_locators.py
@time: 2019-03-14 15:07
@desc:
"""

from selenium.webdriver.common.by import By


# 线损分析→线损浏览:线损汇总
class LineLossBrowseCollectLocators:
    # 查询按钮
    BTN_QRY = (By.XPATH, '//*[@id="search_"]')


# 线损分析→线损浏览:线损查询
class LineLossBrowseQueryLocators:
    # 查询按钮
    BTN_QRY = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/a/span/span')
