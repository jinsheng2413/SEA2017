# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: specialUserBalanceQuery_locators.py
@time: 2018/8/16 0016 14:42
@desc:
"""
from selenium.webdriver.common.by import By


class SpecialUserBalanceQuery_locators:
    # 【查询条件】
    # 用户编号
    QRY_CONS_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户编号')]/../../div[1]/div[1]/input")
    # 用户名称
    QRY_CONS_NAME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户名称')]/../../div[1]/div[1]/input")
    # 终端地址
    QRY_TERMINAL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]/input")
    # 越线类型
    QRY_MORE_BOARD_CATA = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'越限类型')]/../div[1]/div/img")
    QRY_MORE_BOARD_CATA_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'低于告警电量')]/../div[%s]")

    # 召测日期
    QRY_CALL_TEST_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'召测日期')]/../../div[1]/div[1]/div/input")
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')

    # 【操作区】
    BTN_QRY = (
        By.XPATH, "//div[@class=\" x-panel x-panel-noborder\"]//button[contains(text(),'查询')]")
