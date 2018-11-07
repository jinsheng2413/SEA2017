# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lineData_locators.py
@time: 2018/10/30 0030 14:24
@desc:
"""
from selenium.webdriver.common.by import By

#高级应用-->台线系统--》资料维护--》线路资料维护
class LineDataLocators:
    #【查询条件区】
    #变电站
    QRY_TRANSFORMER_SUBSTATION = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'变电站')]/../../div[1]/div[1]//input")
    #负责人
    QRY_MASTER = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'负责人')]/../../div[1]/div[1]//input")
    QRY_MASTER_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'陈越峰')]/../div[contains(text(),'%s')]")
    #线路名称
    QRY_LINE_NAME = (By.XPATH, "//*[@id=\"lineName\"]")
    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
