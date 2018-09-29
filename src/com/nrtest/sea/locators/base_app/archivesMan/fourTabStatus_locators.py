# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: fourTabStatus_locators.py
@time: 2018/9/29 0029 9:47
@desc:
'''
from selenium.webdriver.common.by import By

# 基本应用--》档案管理--》多表合一运行状态
class FourTabStatusLocators:
    #【查询条件区】
    #用户状态
    QRY_USER_STATE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户状态')]/../../div[1]/div[1]//input")
    QRY_USER_STATE_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'正常')]/../div[contains(text(),'%s')]")
    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     