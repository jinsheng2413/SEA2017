# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: interfaceMonitor_locators.py
@time: 2018/10/26 0026 16:01
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用--》接口管理--》接口管理
class InterfaceMonitor_Locators:
    # 【查询条件区】

    # 接口类型
    QRY_INTERFACE_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'接口类型')]/../../div[1]/div[1]//img")
    QRY_INTERFACE_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'调度系统')]/../div[contains(text(),'%s')]")
    # 接口日期从
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'接口日期从')]/../../div[1]/div[1]//input")
    # 到
    QRY_END_TIME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'到')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "//*[text()='查询']")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("interface_dateFrom").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("interface_dateTo").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
