# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: taskTemplateSet_locators.py
@time: 2018/11/20 0020 10:01
@desc:
"""
from selenium.webdriver.common.by import By


# 系统管理→档案核查管理→档案核查模板编制
class TaskTemplateSetLocators:
    # 【查询条件区】

    # 选择模板
    QRY_SELECT_MODULE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'选择模板')]/../../div[1]/div[1]//input")
    QRY_SELECT_MODULE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
