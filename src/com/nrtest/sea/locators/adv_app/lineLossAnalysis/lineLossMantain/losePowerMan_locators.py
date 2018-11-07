# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: losePowerMan_locators.py
@time: 2018/10/31 0031 13:07
@desc:
"""
from selenium.webdriver.common.by import By


# 高级应用-->线损分析--》线损模型维护--》线损模型设计
class LosePowerManLocators:
    # 【查询条件区】
    # 考核单元名称
    QRY_ASSESS_UNIT_NAME = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'考核单元名称')]/../../div[1]/div[1]//input")

    # 考核单元分类
    QRY_ASSESS_UNIT_CLASSFICATION = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[text()='考核单元分类']/../../div[1]/div[1]//img")
    QRY_ASSESS_UNIT_CLASSFICATION_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'台区')]/../div[contains(text(),'%s')]")
    # 组合标志
    QRY_COMBINATION_SIGN = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'组合标志')]/../../div[1]/div[1]//img")
    QRY_COMBINATION_SIGN_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'是')]/../div[contains(text(),'%s')]")
    # 考核单元状态
    QRY_ASSESS_UNIT_STATE = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'考核单元状态')]/../../div[1]/div[1]//img")
    QRY_ASSESS_UNIT_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'启用')]/../div[contains(text(),'%s')]")
    # 台区状态
    QRY_ZONE_AREA_STATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'台区状态')]/../../div[1]/div[1]//img")
    QRY_ZONE_AREA_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'运行')]/../div[contains(text(),'%s')]")
    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
