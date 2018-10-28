# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: terminalOnlineSpied_locators.py
@time: 2018/10/17 0017 8:49
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→终端管理→终端版本召测
class TerminalOnlineSpiedLocators:
    # 【查询条件区】
    # 终端厂商
    QRY_TMNL_MANUFACTURER = (By.XPATH, "//*[@id=\"tmnlFactory\"]")
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//*[@id=\"terminalAddr1\"]")
    # 终端状态
    QRY_TMNL_STATE = (By.XPATH, "//*[@id=\"tmnlOnline\"]")
    # 终端规约
    QRY_TMNL_PROTOCOL = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端规约')]/../../div[1]/div[1]//input")
    # 终端类型
    QRY_TMNL_TYPE = (By.XPATH, '//*[@id="terminalType"]')

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 终端厂商
    TMNL_MANUFACTURER_JS = 'document.getElementById("tmnlFactory").removeAttribute("readonly");'
    # 终端状态
    TMNL_STATE_JS = 'document.getElementById("tmnlOnline").removeAttribute("readonly");'
    # 终端状态
    TMNL_PROTOCOL_JS = 'document.getElementsByTagName(\'input\')[7].removeAttribute(\"readOnly\")'
    # 终端类型
    TMNL_TYPE_JS = 'document.getElementById("terminalType").removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
