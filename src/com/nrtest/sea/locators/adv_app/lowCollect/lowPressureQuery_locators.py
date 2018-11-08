# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: lowPressureQuery_locators.py
@time: 2018-11-01 14:32
@desc:
'''

from selenium.webdriver.common.by import By


# 高级应用--低压采集监控--低压采集查询
class LowPressureQuery_Locators:
    # [显示区]
    # 供电单位
    QRY_ORG = (By.XPATH, "//label[contains(text(),'供电单位')]/../div/input")
    # 台区名称
    QRY_TG_NAME = (By.XPATH, "//label[contains(text(),'台区名称')]/../div/input")
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//label[contains(text(),'终端地址')]/../div/input")
    # 用户编号
    QRY_CONS_NO = (By.XPATH, "//label[contains(text(),'用户编号')]/../div/input")
    # 日期
    QRY_DATE = (By.XPATH, "//label[contains(text(),'日期')]/../div/div/input")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'

    # 【操作区】
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")
