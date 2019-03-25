# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: againDispose_locators.py
@time: 2019-03-13 16:00
@desc:
"""

from selenium.webdriver.common.by import By


# 业务变更→重处理
class AgainDisposeLocators:
    # 提交
    BTN_COMMIT = (By.XPATH, '//*[@id="search_btn"]')
