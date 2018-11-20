# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: ipBlacklistMan_locators.py
@time: 2018/11/20 14:05
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→系统配置管理→IP黑名单管理
class IpBlacklistManLocators:
    # IP地址
    QRY_IP_ADDR = (By.XPATH, '//label[contains(text(),"IP地址")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
