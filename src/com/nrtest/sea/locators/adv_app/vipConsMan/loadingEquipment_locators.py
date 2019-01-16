# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: loadingEquipment_locators.py
@time: 2018-11-05 15:17
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→加载防窃电设备
class LoadingEquipment_locators:
    # [显示区]
    # 供电单位
    QRY_ORG = (By.XPATH, "//input[@id='fqdGw']")
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//input[@id='fqdTD']")

    # 【操作区】
    # 【查询】
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")
    TAB_TWO = (By.XPATH, "(//div[@class='x-grid3-scroller'])[2]")