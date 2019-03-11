# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: collApp_locators.py
@time: 2019/03/06 15:12
@desc:
"""

from selenium.webdriver.common.by import By


class CollOperMain_locators:
    # 采集运维--采集监视--查询按钮
    BTN_SEARCH = (By.XPATH, '//*[@id="lookup"]')
    # 采集运维--采集详情--采集成功率--查询按钮
    BTN_SEARCH1 = (By.XPATH, '//*[@id="search"]')
    # 采集运维--采集详情--采集详情--查询按钮
    BTN_SEARCH2 = (By.XPATH, '//*[@id="searchDetail"]')
