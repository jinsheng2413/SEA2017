# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: differentialloopSettingDetail_locators.py
@time: 2018-11-07 13:50
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用--》重点用户监测--》差动回路明细查询
class DifferentialloopSettingDetail_locators:
    # [显示区]
    # 用户名称
    QRY_CONS_NAME = (By.XPATH, "//input[@id='consName']")

    # 【操作区】
    # 【查询】
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")
