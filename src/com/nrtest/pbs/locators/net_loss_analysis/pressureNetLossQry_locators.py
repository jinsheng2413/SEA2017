# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: pressureNetLossQry_locators.py
@time: 2019-03-15 14:36
@desc:
"""

from selenium.webdriver.common.by import By


# 网损分析→分压网损查询:网损查询
class PressureNetLossQryLocators:
    # 查询按钮
    BTN_QRY = (By.XPATH, '//*[@id="search"]')
