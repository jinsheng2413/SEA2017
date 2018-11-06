# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: meterClockMan_locators.py
@time: 2018/11/2 0002 10:11
@desc:
"""

from selenium.webdriver.common.by import By


# 运行管理-电能表管理-电能表状态查询
class MeterClockManLocators:
    # 【查询条件区】

    # 电表事件类型
    QRY_EVENTTYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'电表事件类型\')]/../../div[1]/div[1]//input")
    QRY_EVENTTYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'时钟电池正常')]/../div[contains(text(),'%s')]")
    # 终端厂家
    QRY_TMNLFACORY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'终端厂家\')]/../../div[1]/div[1]//img")
    QRY_TMNLFACORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东方电子')]/../div[contains(text(),'%s')]")
    # 电表厂家
    QRY_METERFACTORY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'电表厂家\')]/../../div[1]/div[1]//img")
    QRY_METERFACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'ABB公司\')]/../div[contains(text(),'%s')]")
    # 终端地址
    QRY_TMNLADDR = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'终端地址\')]/../../div[1]/div[1]//input")
    # 用户编号
    QRY_USERNO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'用户编号\')]/../../div[1]/div[1]//input")
    # 电表资产号
    QRY_METERNO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'电表资产号\')]/../../div[1]/div[1]//input")
    # 日期
    QRY_DATE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'日期\')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])")

    # 【js区】
    # 日期
    START_DATE_JS = 'document.getElementById(\'meterClockDate\').removeAttribute("readonly");'
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
