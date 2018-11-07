# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: readCompleteRate_locators.py
@time: 2018/10/10 0010 9:57
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→采集质量分析→采集完整率
class ReadCompleteRateLocators:
    # 【查询条件区】
    # 日期时间
    QRY_DATE_TIME_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'日期时间')]/../../div[1]/div[1]//input)[1]")
    # 日期时间
    QRY_DATE_TIME_DETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'日期时间')]/../../div[1]/div[1]//input)[2]")

    # 芯片厂家
    QRY_CHIP_FACTORY = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'芯片厂家')]/../../div[1]/div[1]//input)[1]")
    QRY_CHIP_FACTORY_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东软')]/../div[contains(text(),'%s')])[2]")

    # 蕊片厂家
    QRY_CHIP_FACTORY_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'芯片厂家')]/../../div[1]/div[1]//input)[2]")
    QRY_CHIP_FACTORY_COUNT_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东软')]/../div[contains(text(),'%s')])[2]")

    # 蕊片厂家
    QRY_CHIP_FACTORY_DETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'蕊片厂家')]/../../div[1]/div[1]//input)[4]")
    QRY_CHIP_FACTORY_DETAIL_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东软')]/../div[contains(text(),'%s')])[4]")

    # 终端厂家
    QRY_TMNL_FACTORY = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端厂家')]/../../div[1]/div[1]//input)[1]")
    QRY_TMNL_FACTORY_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东方电子')]/../div[contains(text(),'%s')])[1]")

    # 终端厂家
    QRY_TMNL_FACTORY_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端厂家')]/../../div[1]/div[1]//input)[2]")
    QRY_TMNL_FACTORY_COUNT_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东方电子')]/../div[contains(text(),'%s')]")

    # 终端厂家
    QRY_TMNL_FACTORY_DETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端厂家')]/../../div[1]/div[1]//input)[3]")
    QRY_TMNL_FACTORY_DETAIL_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东方电子')]/../div[contains(text(),'%s')])[3]")
    # 通信方式
    QRY_COMMUNICATION_MODE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'通信方式')]/../../div[1]/div[1]//input)[1]")
    QRY_COMMUNICATION_MODE_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'电话网')]/../div[contains(text(),'%s')])[1]")
    # 通信方式
    QRY_COMMUNICATION_MODE_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'通信方式')]/../../div[1]/div[1]//input)[2]")
    QRY_COMMUNICATION_MODE_COUNT_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'电话网')]/../div[contains(text(),'%s')]")

    # 通信方式
    QRY_COMMUNICATION_MODE_DETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'通信方式')]/../../div[1]/div[1]//input)[2]")
    QRY_COMMUNICATION_MODE_DETAIL_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'电话网')]/../div[contains(text(),'%s')])[2]")
    #
    QRY_ = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")
    # 用户类型
    QRY_USER_TYPE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'用户类型')]/../../div[1]/div[1]//input)[1]")
    QRY_USER_TYPE_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')])[1]")

    # 用户类型
    QRY_USER_TYPE_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'用户类型')]/../../div[1]/div[1]//input)[2]")
    QRY_USER_TYPE_COUNT_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'专变\')]/../div[contains(text(),'%s')]")

    # 用户类型
    QRY_USER_TYPE_DETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'用户类型')]/../../div[1]/div[1]//input)[3]")
    QRY_USER_TYPE_DETAIL_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')])[3]")
    # 开始时间
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始时间')]/../../div[1]/div[1]//input")
    # 结束时间
    QRY_END_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'结束时间')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    BTN_QRY_COUNT = (By.XPATH,
                     "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")
    BTN_QRY_DETAIL = (By.XPATH,
                      "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[3]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = "document.getElementsByTagName('input')[11].removeAttribute(\"readonly\");"
    # 结束时间，删除readonly属性
    END_DATE_JS = "document.getElementsByTagName('input')[12].removeAttribute(\"readonly\");"
    JS_COUNT = "document.getElementById('rcrcReadDate').removeAttribute(\"readOnly\")"
    JS_DETAIL = "document.getElementById('rcrdStatDate').removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_COUNT_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[6]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
