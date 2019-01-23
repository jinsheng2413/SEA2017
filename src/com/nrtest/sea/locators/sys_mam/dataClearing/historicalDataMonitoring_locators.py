# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: historicalDataMonitoring_locators.py
@time: 2018/11/20 0020 11:30
@desc:
"""
from selenium.webdriver.common.by import By


# 系统管理→数据清理管理→历史数据监控
class HistoricalDataMonitoringLocators:
    # 【查询条件区】
    # 表名称
    QRY_LIST_NAME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'表名称')]/../../div[1]/div[1]//input")
    # 数据来源
    QRY_DATA_SRC = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'数据来源')]/../../div[1]/div[1]//img")
    QRY_DATA_SRC_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'采集生产库')]/../div[contains(text(),'%s')]")
    # 数据组
    QRY_DATA_GROUP = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'数据组')]/../../div[1]/div[1]//img")
    QRY_DATA_GROUP_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'标准数据')]/../div[contains(text(),'%s')]")
    # 开始日期
    QRY_START_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始日期')]/../../div[1]/div[1]//input")
    # 截至日期
    QRY_END_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'截止日期')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByName(\'findDateS\')[0].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByName(\"findDateS\")[1].removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
