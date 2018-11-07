# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: terminalPassword__locators.py
@time: 2018/10/17 0017 10:59
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→终端管理→终端在线监视

class TerminalPasswordLocators:
    # 【查询条件区】
    # 日期
    QRY_DATE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'日期')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】

    JS = "document.getElementsByTagName('input')[4].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
