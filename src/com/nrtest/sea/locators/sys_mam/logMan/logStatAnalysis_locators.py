# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: logStatAnalysis_locators.py
@time: 2018/11/21 0021 14:06
@desc:
"""
from selenium.webdriver.common.by import By

# 系统管理--》日志管理--》日志统计分析
class LogStatAnalysis_fail_Locators:
    #【查询条件区】
    #查询日期
    QRY_DATE = (By.XPATH, "//*[@id=\"logStatAnalysis.loginFailQryDate\"]")


    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("logStatAnalysis.loginFailQryDate").removeAttribute("readonly");'
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
# 系统管理--》日志管理--》日志统计分析
class LogStatAnalysis_list_Locators:
    #【查询条件区】
    #查询日期
    QRY_QUERY_DATE = (By.XPATH, "//*[@id=\"logStatAnalysis.startDate1\"]")
    #至
    QRY_TO = (By.XPATH, "//*[@id=\"logStatAnalysis.endDate1\"]")


    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("logStatAnalysis.startDate1").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("logStatAnalysis.endDate1").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")

# 系统管理--》日志管理--》日志统计分析
class LogStatAnalysis_man_Locators:
    #【查询条件区】
    # 查询日期
    QRY_QUERY_DATE = (By.XPATH, "//*[@id=\"logStatAnalysis.startDate2\"]")
    #至
    QRY_TO = (By.XPATH, "//*[@id=\"logStatAnalysis.endDate2\"]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//button[contains(text(),'查询')])[2]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("logStatAnalysis.startDate2").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("logStatAnalysis.endDate2").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     