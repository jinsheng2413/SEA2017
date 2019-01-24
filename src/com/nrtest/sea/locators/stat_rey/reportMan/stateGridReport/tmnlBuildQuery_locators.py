# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: tmnlBuildQuery_locators.py
@time: 2018/11/8 8:58
@desc:
"""
from selenium.webdriver.common.by import By


# 统计查询→报表管理→国网报表→智能电能表及终端设备建设情况
class TmnlBuildQueryLocators:
    # 【查询条件区】
    #
    QRY_DATE_S = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'日期\')]/../../div[1]/div[1]//input")
    QRY_DATE_E = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'到\')]/../../div[1]/div[1]//input")
    # 终端类型
    QRY_TMNL_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'终端类型\')]/../../div[1]/div[1]//input")
    QRY_TMNL_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'专变终端\')]/../div[contains(text(),'%s')]")

    # 终端厂家
    QRY_TMNL_FACTORY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'终端厂家\')]/../../div[1]/div[1]//input")
    QRY_TMNL_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'东方电子\')]/../div[contains(text(),'%s')]")
    # 统计口径
    QRY_STAT_SCOPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'统计口径\')]/../../div[1]/div[1]//input")
    QRY_STAT_SCOPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'直供直管\')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[6].removeAttribute("readonly");'
    END_DATE_JS = 'document.getElementsByTagName(\'input\')[7].removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
