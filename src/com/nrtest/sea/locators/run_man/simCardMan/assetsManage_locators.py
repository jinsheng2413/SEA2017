# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: assetsManage_locators.py
@time: 2018/11/8 0008 14:53
@desc:
"""
from selenium.webdriver.common.by import By

#运行管理-->SIM卡管理-->资产管理
class AssetsManageLocators:
    #【查询条件区】
    # 所属系统
    QRY_SUBORDINATE_SYSTEM = (By.XPATH, "//*[@name=\"simSystemCombox\"]")
    QRY_SUBORDINATE_SYSTEM_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'营销系统')]/../div[contains(text(),'%s')]")
    #SIM卡号段
    QRY_SIM_CARD_NO = (By.XPATH, "//*[@id=\"simCardStart\"]")
    #至
    QRY_SIM_CARD_NO_TO = (By.XPATH, "//*[@id=\"simCardEnd\"]")
    #SIM卡状态
    QRY_SIM_CARD_STATUS = (By.XPATH,'//*[@name=\"simCardStatusCombox\"]')
    QRY_SIM_CARD_STATUS_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'运行')]/../div[contains(text(),'%s')]")
    #运营商
    QRY_OPERATOR = (By.XPATH, "//*[@name=\"simBusinessCombox\"]")
    QRY_OPERATOR_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'移动段号')]/../div[contains(text(),'%s')]")
    #导入时间
    QRY_LEAD_TO_TIME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'导入日期')]/../../div[1]/div[1]//input")
    # 时间至
    QRY_TIME_TO = (
    By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'至')]/../../div[1]/div[1]//input)[2]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[8].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName(\'input\')[9].removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     