# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: simInstallStat_locators.py
@time: 2018/11/9 0009 9:09
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→SIM卡管理→运行情况分析→安装情况统计
class SimInstallStatLocators:
    #【查询条件区】

    #运营商
    QRY_OPERATOR = (By.XPATH, "//*[@name=\"simBusinessCombox\"]")
    QRY_OPERATOR_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'联通段号')]/../div[contains(text(),'%s')]")


    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     