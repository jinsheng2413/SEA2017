# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: terminalVersion_locators.py
@time: 2018/10/17 0017 11:36
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→终端管理→终端离线明细
class TerminalVersionLocators:
    # 【查询条件区】
    # 用户编号
    QRY_USER_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户编号')]/../../div[1]/div[1]//input")
    # 终端地址
    QRY_TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]//input")

    # 查询日期
    QRY_DATE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'查询日期')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    JS = "document.getElementsByTagName('input')[6].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
