# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: dataCheckTaskSet_locators.py
@time: 2018/11/19 0019 14:23
@desc:
"""
from selenium.webdriver.common.by import By


# 系统管理--》档案核查管理--》档案任务核查编制
class DataCheckTaskSetLocators:
    # 【查询条件区】
    # 台区编号
    QRY_ZONE_AREA_NO = (By.XPATH, "//*[@name=\"lockNoText\"]")
    # 任务模板
    QRY_ = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")
    QRY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')]")

    # 任务来源
    QRY_TASK_FROM = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'任务来源')]/../../div[1]/div[1]//input")
    QRY_TASK_FROM_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'人工任务')]/../..//div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
