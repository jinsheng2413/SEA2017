# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: readIntimeRate_locators.py
@time: 2018/10/11 0011 8:27
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→采集质量分析→采集及时率
class ReadIntimeRate_Locators:
    # 【查询条件区】
    # 用户类型
    QRY_CONS_TYPE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'用户类型')]/../../div[1]/div[1]//input)[1]")
    QRY_CONS_TYPE_VALUE = (
        By.XPATH,
        "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'居民用户（ E 类）')]/../div[contains(text(),'%s')]")
    # 终端厂家
    QRY_TMNL_FACTORY = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端厂家')]/../../div[1]/div[1]//input)[1]")
    QRY_TMNL_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东方电子')]/../div[contains(text(),'%s')]")

    # 芯片厂家
    QRY_CHIP_FACTORY = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'芯片厂家')]/../../div[1]/div[1]//input)[1]")
    QRY_CHIP_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'晓程')]/../div[contains(text(),'%s')]")

    # 日期时间
    QRY_DATE_TIME = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'日期时间')]/../../div[1]/div[1]//input)[1]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[10].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
