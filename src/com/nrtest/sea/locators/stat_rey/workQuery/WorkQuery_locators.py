# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: WorkQuery_locators.py
@time: 2018/10/31 14:26
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→工单查询→工单查询
class WorkCountLocators:
    # 【查询条件区】
    #
    QRY_DATE = (
    By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),\'日   期\')]/../../div[1]/div[1]//input)[1]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[5].removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")


class WorkQueryLocators:
    # 【查询条件区】
    # 异常编号
    QRY_ABNORMAL_NO = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'异常编号\')]/../../div[1]/div[1]//input")
    # 异常状态
    QRY_ABNORMAL_STATUS = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'异常状态\')]/../../div[1]/div[1]//input")
    QRY_ABNORMAL_STATUS_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'新异常\')]/../div[contains(text(),'%s')]")
    # 日期
    QRY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),\'日   期\')]/../../div[1]/div[1]//input)[2]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById(\'workQueryDate\').removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
