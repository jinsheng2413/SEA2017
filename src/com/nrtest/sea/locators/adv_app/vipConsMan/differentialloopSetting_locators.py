# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: differentialloopSetting_locators.py
@time: 2018-11-06 9:44
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→差动回路设置
class DifferentialloopSetting_locators:
    # [显示区]
    # 节点名
    QRY_ORG = (By.XPATH, "//input[@id='cdOrgName']")
    # 用户编号
    QRY_CONS_NO = (By.XPATH, "//input[@id='yhbh']")
    # 用户名称
    QRY_CONS_NAME = (By.XPATH, "//input[@id='yhmc']")
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//input[@id='zddz']")
    # 终端资产号
    QRY_TMNL_ASSET_NO = (By.XPATH, "//input[@id='zdzch']")

    # 【操作区】
    # 【查询】
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")
    TAB_TWO = (By.XPATH, "(//div[@class='x-grid3-scroller'])[2]")
    TAB_THREE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[3]")
