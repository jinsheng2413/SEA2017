# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulPropMain_locators.py
@time: 2018/11/2 0002 9:59
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理--》采集信道管理--》通信模块管理--》通信模块属性维护
class CommunicationModuleBaseInformationMantainLocators:
    # 【查询条件区】
    # 模块版本

    # 模块厂商
    QRY_MODULE_FACTORY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'模块厂商')]/../../div[1]/div[1]//input")
    QRY_MODULE_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东软')]/../div[contains(text(),'%s')]")
    # 模块属性标识
    QRY_MODULE_ATTRBUTE_SIGN = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'模块属性标识')]/../../div[1]/div[1]//input")
    # 模块类型
    QRY_MODULE_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'模块类型')]/../../div[1]/div[1]//input")
    QRY_MODULE_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'窄带载波')]/../div[contains(text(),'%s')]")

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
    TAB_ONE = (By.XPATH,
               '(//div[text()=\'模块属性标识\']/ancestor::div[@class=\"x-panel-body x-panel-body-noheader\"]//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")


class ModuleAttributeRelationshipMantainLocators:
    # 【查询条件区】
    # 终端厂商
    QRY_TMNL_FACTORY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端厂商')]/../../div[1]/div[1]//img")
    QRY_TMNL_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'东方电子')]/../div[contains(text(),'%s')]")
    # 终端地址
    QRY_TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    # 【js区】
    # 开始时间，删除readonly属性
    TMNL_FACTORY_JS = "document.getElementsByClassName(\" x-form-text x-form-field x-trigger-noedit x-form-focus\")[0].removeAttribute(\"readonly\");"
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH,
               '(//font[text()= \'终端信息\']/ancestor::div[@class=\"x-panel-bwrap \"]//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
