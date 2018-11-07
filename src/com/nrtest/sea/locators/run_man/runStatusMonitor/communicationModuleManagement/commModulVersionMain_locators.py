# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulVersionMain_locators.py
@time: 2018/11/6 0006 14:17
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理--》采集信道管理--》通信模块管理--》本地通信模块版本信息召测
class CommModulVersionMainLocators:
    # 【查询条件区】
    # 终端厂商
    QRY_TMNL_FACTORY = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端厂商')]/../../div[1]/div[1]//img")
    QRY_TMNL_FACTORY_VALUE = (
        By.XPATH,
        "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'江苏林洋电子有限公司')]/../div[contains(text(),'%s')]")
    # 终端类型
    QRY_TMNL_TYPE = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端类型')]/../../div[1]/div[1]//img")
    QRY_TMNL_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'%s')]//img")
    # 终端地址
    QRY_TMNL_ADDR = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
