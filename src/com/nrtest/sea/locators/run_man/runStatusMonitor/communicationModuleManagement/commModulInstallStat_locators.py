# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulInstallStat_locators.py
@time: 2018/11/6 0006 11:16
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→采集信道管理→通信模块管理→通信模块安装统计
class CommModulInstallStatLocators:
    # 【查询条件区】
    # 日期
    QRY_DATE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'日期')]/../../div[1]/div[1]//input")
    # 模块类型
    QRY_MODULE_TYPE = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'模块类型')]/../../div[1]/div[1]//img")
    QRY_MODULE_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'窄带载波')]/../div[contains(text(),'%s')]")
    # 模块厂商
    QRY_MODULE_FACTORY = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'模块厂商')]/../../div[1]/div[1]//img")
    QRY_MODULE_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东软')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[4].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
