# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: changeLossBrowse_locators.py
@time: 2019-03-14 16:33
@desc:
"""

from selenium.webdriver.common.by import By


# 线损分析→变损浏览:变损汇总
class ChangeLossBrowseCollectLocators:
    # 查询按钮
    BTN_QRY = (By.XPATH, '//*[@id="search"]')


# 线损分析→变损浏览:变损查询
class ChangeLossBrowseQueryLocators:
    # 查询按钮
    BTN_QRY = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/button')
