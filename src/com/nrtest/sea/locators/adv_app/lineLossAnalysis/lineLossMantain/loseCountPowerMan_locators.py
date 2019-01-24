# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: loseCountPowerMan_locators.py
@time: 2018/11/1 0001 16:32
@desc:
"""
from selenium.webdriver.common.by import By


# 高级应用-->线损分析→线损模型维护→线损计算模型管理

class LoseCountPowerManLocators:
    # 【查询条件区】
    # 台区运行状态
    QRY_TG_STATUS = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'台区运行状态')]/../../div[1]/div[1]//input")
    QRY_TG_STATUS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'运行')]/../div[contains(text(),'%s')]")
    # 责任人工号
    QRY_PERSON_RESP_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'责任人工号')]/../../div[1]/div[1]//input")
    # 台区编码
    QRY_TG_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'台区编码')]/../../div[1]/div[1]//input")
    # 台区名称
    QRY_TG_NAME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'台区名称')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
