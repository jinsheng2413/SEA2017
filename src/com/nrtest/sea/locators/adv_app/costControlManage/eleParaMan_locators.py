# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: eleParaMan_locators.py
@time: 2018/9/29 0029 13:46
@desc:
"""
from selenium.webdriver.common.by import By


# 高级应用→费控管理→本地费控→电价参数管理
class EleParaManLocators:
    # 【查询条件区】
    # 起始日期
    QRY_START_TIME_ONE = (By.XPATH, "// *[ @ id=\"erateParamMainStartDate\"]")

    QRY_START_TIME_TWO = (By.XPATH, "//*[@id=\"erateParamMainStartDate_two\"]")

    # 终止日期
    QRY_END_TIME_ONE = (By.XPATH, "//*[@id=\"erateParamMainEndDate\"]")
    QRY_END_TIME_TWO = (By.XPATH, "//*[@id=\"erateParamMainEndDate_two\"]")
    QRY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')]")
    # 是否已生成参数
    QRY_OR_COMEINTO_PARA_ONE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'是否已生成参数')]/../../div[1]/div[1]//input)[1]")
    QRY_OR_COMEINTO_PARA_ONE_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')])[2]")
    QRY_OR_COMEINTO_PARA_TWO = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'是否已生成参数')]/../../div[1]/div[1]//input)[2]")
    QRY_OR_COMEINTO_PARA_TWO_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')])[2]")

    # 【操作区】
    BTN_QRY_ONE = (
        By.XPATH, "(//*[@class=\"x-column-inner\"]//button[contains(text(),'查询')])[1]")
    BTN_QRY_TWO = (
        By.XPATH, "(//*[@class=\"x-column-inner\"]//button[contains(text(),'查询')])[1]")
    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS_ONE = 'document.getElementById("erateParamMainStartDate").removeAttribute("readonly");'
    START_DATE_JS_TWO = 'document.getElementById("erateParamMainStartDate_two").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS_ONE = 'document.getElementById("erateParamMainEndDate").removeAttribute("readonly");'
    END_DATE_JS_TWO = 'document.getElementById("erateParamMainEndDate_two").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
