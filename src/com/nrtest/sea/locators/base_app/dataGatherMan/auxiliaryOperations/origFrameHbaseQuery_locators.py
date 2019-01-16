# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: origFrameHbaseQuery_locators.py
@time: 2018/11/9 0009 15:40
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→采集运维平台→辅助运维→报文查询
class OrigFrameHbaseQueryLocators:
    #【查询条件区】
    #终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//*[@id=\"orgFrameQueryTmnlAddr\"]")
    #报文类型
    QRY_MESSAGE_TYPE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'报文类型')]/../../div[1]/div[1]//input")
    QRY_MESSAGE_TYPE_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'复位命令')]/../div[contains(text(),'%s')]")
    #查询日期
    QRY_QUERY_TIME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'查询日期')]/../../div[1]/div[1]//input")
    #从
    QRY_FROM = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'从')]/../../div[1]/div[1]//input")
    #到
    QRY_TO = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'d到')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[5].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     