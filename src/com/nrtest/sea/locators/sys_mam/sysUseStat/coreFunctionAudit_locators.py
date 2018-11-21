# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: coreFunctionAudit_locators.py
@time: 2018/11/21 0021 9:55
@desc:
"""
from selenium.webdriver.common.by import By

# 系统管理→系统使用情况统计→系统使用情况统计
class CoreFunctionAuditLocators:
    #【查询条件区】
    #操作员
    QRY_PERFORMER = (By.XPATH, "//*[@id=\"menuCoreUseStat_staffField_1\"]")
    #访问日期
    QRY_VISIST_DATE = (By.XPATH, "//*[@id=\"menuCoreUseStat_startDate_1\"]")
    #到
    QRY_TO = (By.XPATH, "//*[@id=\"menuCoreUseStat_endDate_1\"]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("menuCoreUseStat_startDate_1").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("menuCoreUseStat_endDate_1").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     