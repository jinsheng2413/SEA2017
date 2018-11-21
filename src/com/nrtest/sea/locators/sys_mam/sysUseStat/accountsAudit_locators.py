# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: accountsAudit_locators.py
@time: 2018/11/21 0021 10:34
@desc:
"""
from selenium.webdriver.common.by import By


# 系统管理→系统使用情况统计→账号审计
class AccountsAuditLocators:
    #【查询条件区】
    #时间
    QRY_DATE = (By.XPATH, "(//*[@id=\"账号审计\"]//input)[4]")
    #账号状态
    QRY_ACCOUNT_STATUS = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'账号状态')]/../../div[1]/div[1]//input")
    QRY_ACCOUNT_STATUS_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'正常')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[6].removeAttribute("readonly");'
    START_DATE_I_JS = 'document.getElementsByTagName(\'input\')[7].removeAttribute("readonly");'

     
     
     
     
     