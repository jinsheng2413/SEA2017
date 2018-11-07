# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: lowPressureMonitor_locators.py
@time: 2018-11-01 10:39
@desc:
'''

from selenium.webdriver.common.by import By


# 高级应用--低压采集监控--配置采集任务

class LowPressureMonitor_Locators:
    # [显示区]
    # 供电单位
    QRY_ORG = (By.XPATH, "//input[@id='monitorOrgNameText']")
    # 台区名称
    QRY_TG_NAME = (By.XPATH, "//input[@id='monitorTgNameText']")
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//input[@id='monitorTmnlAddrText']")
    # 用户定义类别
    QRY_CONS_DEFINE_TYPE = (
        By.XPATH, "//label[contains(text(),'用户定义类别')]/../div/div/input")
    # 值（用户定义类别）
    QRY_CONS_DEFINE_TYPE_VALUE = (
        By.XPATH,
        "(//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'已定义')])[1]/../div[contains(text(),'%s')]")

    # 【操作区】
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")
