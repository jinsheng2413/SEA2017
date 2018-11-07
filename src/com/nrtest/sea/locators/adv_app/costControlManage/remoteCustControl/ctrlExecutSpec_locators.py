# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: ctrlExecutSpec_locators.py
@time: 2018/9/30 0030 11:04
@desc:
"""
from selenium.webdriver.common.by import By


# 高级应用--》费控管理--》远程费控--》专变用户远程费控执行
class CtrlExecutSpecLocators:
    # 【查询条件区】

    # 执行状态
    QRY_EXE_STATUS = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'执行状态')]/../../div[1]/div[1]//input")
    QRY_EXE_STATUS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'待下发命令')]/../div[contains(text(),'%s')]")
    # 用户编号
    QRY_USER_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户编号')]/../../div[1]/div[1]//input")
    # 控制类型
    QRY_CONTROL_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'控制类型')]/../../div[1]/div[1]//input")
    QRY_CONTROL_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'预警')]/../div[contains(text(),'%s')]")
    # 用户名称
    QRY_USER_NAME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户名称')]/../../div[1]/div[1]//input")
    # 终端地址
    QRY_TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]//input")
    # 开始时间
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始时间')]/../../div[1]/div[1]//input")
    # 结束时间
    QRY_END_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'结束时间')]/../../div[1]/div[1]//input")
    # 工单号
    QRY_WORK_ORDER = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'工单号')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("startDateTimeSpec").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("endDateTimeSpec").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
