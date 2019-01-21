# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkReduceApplication_locators.py
@time: 2018/11/20 0020 10:20
@desc:
"""
from selenium.webdriver.common.by import By


# 系统管理→档案核查管理→考核减免申请
class CheckReduceApplicationLocators:
    # 【查询条件区】
    # 开始日期
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始日期')]/../../div[1]/div[1]//input")

    # 结束日期
    QRY_END_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'结束日期')]/../../div[1]/div[1]//input")
    # 申请单号
    QRY_APPLY_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'申请单号')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[4].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName(\'input\')[5].removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
