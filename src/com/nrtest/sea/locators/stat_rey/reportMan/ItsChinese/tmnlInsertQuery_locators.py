# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: tmnlInsertQuery_locators.py
@time: 2018/11/7 0007 14:58
@desc:
"""
from selenium.webdriver.common.by import By


# 统计查询-->报表管理-->国网报表-->智能电能表及终端设备接入情况
class TmnlInsertQueryLocators:
    #【查询条件区】
    #日期
    QRY_DATE = (By.XPATH, "//input[@name=\"tmnlInsertQueryDate1\"]")
    #到
    QRY_TO = (By.XPATH,'//input[@name="tmnlInsertQueryDate2"]')
    #终端类型
    QRY_TMNL_TYPE = (By.XPATH, "//input[@name=\"insertTmnlTypeCombo\"]")
    QRY_TMNL_TYPE_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'集中器')]/../..//div[contains(text(),'%s')]/img")
    # 终端厂家
    QRY_TMNL_FACTORY = (By.XPATH, "//input[@name=\"insertTmnlFacCombo\"]")
    QRY_TMNL_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'东方电子')]/../..//div[contains(text(),'%s')]/img")

    # 统计口径
    QRY_COUNT_CALIBER = (By.XPATH, "//input[@name=\"insertStatScopeCombo\"]")
    QRY_COUNT_CALIBER_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'全口径')]/../..//div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByName(\'tmnlInsertQueryDate1\')[0].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByName(\'tmnlInsertQueryDate2\')[0].removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     