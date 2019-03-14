# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: handworkEnterPlanValue_locators.py
@time: 2019-03-13 14:17
@desc:
"""

from selenium.webdriver.common.by import By


# 业务变更→手工录入计划值
class HandworkEnterPlanValueLocators:
    # 查询按钮
    BTN_QUERY = (By.XPATH, '//*[@id="search_btn"]')
