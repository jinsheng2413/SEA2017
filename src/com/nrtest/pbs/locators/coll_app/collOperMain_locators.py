# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: collOperMain_locators.py
@time: 2019/03/06 15:12
@desc:
"""

from selenium.webdriver.common.by import By


class CollOperMain_locators:
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//*[@id="lookup"]')
