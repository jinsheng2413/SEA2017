# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: PrePaidStatus_locators.py
@time: 2018/9/29 0029 15:07
@desc:
'''
from selenium.webdriver.common.by import By


class NewPrePaidStatusLocators:
    #【查询条件区】
    # 控制类别
    QRY_CONTROL_TYPE_TWO = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'控制类别')]/../../div[1]/div[1]//input)[2]")
    QRY_CONTROL_TYPE_VALUE_TWO = (By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'高压远程费控')]/..)[2]/div[%s]")
    #开始时间
    QRY_START_TIME_ONE = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'从')]/../../div[1]/div[1]//input)[1]")
    QRY_START_TIME_TWO = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'从')]/../../div[1]/div[1]//input)[2]")
    #结束时间
    QRY_END_TIME_ONE = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'到')]/../../div[1]/div[1]//input)[1]")
    QRY_END_TIME_TWO = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'到')]/../../div[1]/div[1]//input)[2]")
    #控制类别
    QRY_CONTROL_TYPE_ONE = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'控制类别')]/../../div[1]/div[1]//input)[1]")
    QRY_CONTROL_TYPE_VALUE_ONE = (By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'高压远程费控')]/..)[1]/div[%s]")


    # 【操作区】
    BTN_QRY_ONE = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    BTN_QRY_TWO = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_TWO_JS = "document.getElementsByName('dateFieldFrom1')[0].removeAttribute(\"readonly\");"
    START_DATE_ONE_JS = "document.getElementsByName('dateField_1S')[0].removeAttribute(\"readonly\");"

    # 结束时间，删除readonly属性
    END_DATE_TWO_JS = "document.getElementsByName('dateFieldTo1')[0].removeAttribute(\"readonly\");"
    END_DATE_ONE_JS = "document.getElementsByName('dateFieldE')[0].removeAttribute(\"readonly\");"
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_TWO = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[7]')

    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     