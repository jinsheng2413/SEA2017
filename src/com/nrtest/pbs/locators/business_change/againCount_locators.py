# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: againCount_locators.py
@time: 2019-03-14 13:58
@desc:
"""

from selenium.webdriver.common.by import By


# 业务变更→重计算
class AgainCountLocators:
    # 提交
    BTN_COMMIT = (By.XPATH, '//*[@id="search_btn"]')
