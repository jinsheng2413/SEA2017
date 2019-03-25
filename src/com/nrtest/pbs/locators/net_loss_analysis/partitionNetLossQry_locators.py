# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: partitionNetLossQry_locators.py
@time: 2019-03-15 14:11
@desc:
"""

from selenium.webdriver.common.by import By


# 网损分析→分区网损查询:网损查询
class PartitionNetLossQryLocators:
    # 查询按钮
    BTN_QRY = (By.XPATH, '//*[@id="search"]')
