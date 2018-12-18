# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: terminalDataQueryLocators.py
@time: 2018/8/10 0002 09:30
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→终端数据查询
class TerminalDataQueryLocators:
    # 页面元素
    # 终端资产号
    QRY_TMNL_ASSET_NO = (By.XPATH, '//input[@id="nari.synthQuery.tmnlAssetNo"]')
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, '//input[@id="nari.synthQuery.terminalAddr"]')
