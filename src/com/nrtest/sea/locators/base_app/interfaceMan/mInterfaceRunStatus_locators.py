# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mInterfaceRunStatus_locators.py
@time: 2018-10-30 10:46
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→接口管理→其他业务接口→接口运行状态
class MInterfaceRunStatusLocators:
    # 【显示区】
    # 业务系统
    QRY_BUSINESS_SYSTEM = (
        By.XPATH, "//label[contains(text(),'业务系统')]/../div/div/input")
    # 执行状态的值
    QRY_BUSINESS_SYSTEM_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'数据中心')]/../div[contains(text(),'%s')]")

    # 服务对象名称
    QRY_SERVICE_NAME = (
        By.XPATH, "//label[contains(text(),'服务对象名称')]/../div/div/input")
    # 执行状态的值
    QRY_SERVICE_NAME_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'装接流程')]/../div[contains(text(),'%s')]")

    # 【操作区】
    # 查询
    BTN_QRY = (By.XPATH, "//button[contains(text(),'查询')]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')
