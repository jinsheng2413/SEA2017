# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: metclassfiy_locators.py
@time: 2018/10/16 0016 14:11
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→电能表分级归类管理
class MetclassfiyLocators:
    # 【查询条件区】
    # 模板名称
    QRY_TEMPLET_NAME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'模板名称')]/../../div[1]/div[1]//input")
    # 电能表类型
    QRY_METER_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'电能表类型')]/../../div[1]/div[1]//img")
    QRY_METER_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'13版三相电能表')]/../div[contains(text(),'%s')]")
    # 操作
    QRY_PERFORMER = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'操作')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
