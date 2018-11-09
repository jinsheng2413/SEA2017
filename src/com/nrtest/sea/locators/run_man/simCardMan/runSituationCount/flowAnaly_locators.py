# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: flowAnaly_locators.py
@time: 2018/11/9 0009 9:42
@desc:
"""
from selenium.webdriver.common.by import By

# 运行管理-->SIM卡管理-->运行情况分析-->流量分析
class FlowCountLocators:
    #【查询条件区】
    #月份
    QRY_MONTH = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'月份')]/../../div[1]/div[1]//input)[1]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[4].removeAttribute("readonly");'
    #【显示区】
    TAB_ONE = (By.XPATH, '(//*[@class=\"x-toolbar-left-row\"]//*[text()=\'流量统计\']/ancestor::div[@class=\" x-panel x-grid-with-col-lines x-grid-panel x-border-panel\"]//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
class FlowDetailLocators:
    #【查询条件区】
    #月份
    QRY_MONTH = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'月份')]/../../div[1]/div[1]//input)[2]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[6].removeAttribute("readonly");'
    #【显示区】
    TAB_ONE = (By.XPATH, '(//*[@class=\"x-toolbar-left-row\"]//*[text()=\'流量明细\']/ancestor::div[@class=\" x-panel x-grid-with-col-lines x-grid-panel x-border-panel\"]//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")

class SIMFlowCountLocators:
    #【查询条件区】
    #sim卡号
    QRY_SIM_NO = (By.XPATH,'//*[@id="simOverTrafficNo"]')
    #终端地址
    QRY_TMNL_ADDR = (By.XPATH,'//*[@id="terminalAddr"]')

    #统计时间
    QRY_COUNT_TIME = (By.XPATH, "//*[@id=\"simChargeDate\"]")

    # 【操作区】
    BTN_QRY = (By.XPATH,"(//*[text()='查询'])[2]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById(\'simChargeDate\').removeAttribute("readonly");'
    #【显示区】
    TAB_ONE = (By.XPATH, '//*[text()=\'终端资产编号\']/ancestor::div[@class=\" x-panel  x-grid-with-col-lines x-grid-panel x-border-panel\"]//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     