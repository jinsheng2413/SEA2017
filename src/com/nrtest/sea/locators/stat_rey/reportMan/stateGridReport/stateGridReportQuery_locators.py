# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: stateGridReportQuery_locators.py
@time: 2018/11/8 11:30
@desc:
"""
from selenium.webdriver.common.by import By


# 统计查询--》报表管理--》国网报表--》国网报表新
class StateGridReportQueryLocators:
    # 【查询条件区】
    # 报表管理
    QRY_REPORT_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'报表类型\')]/../../div[1]/div[1]//input")
    QRY_REPORT_TYPE_VALUE = (
        By.XPATH,
        "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'四表合一采集质量监测报表\')]/../div[contains(text(),'%s')]")
    # 日期
    QRY_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'日期\')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById(\'sysOtherDateByDay\').removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
