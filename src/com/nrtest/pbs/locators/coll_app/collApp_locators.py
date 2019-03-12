# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
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
    # 采集运维--采集通道监视--通道状态查询
    BTN_SEARCH3 = (By.XPATH, '//*[@id="search"]')
    # 采集运维--历史报文
    BTN_SEARCH4 = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/table/tbody/tr/td/button')
