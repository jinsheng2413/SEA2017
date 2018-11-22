# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userOperationMan_locators.py
@time: 2018/11/20 14:42
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→系统配置管理→用户操作监测
class UserOperationMonitorLocators:
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 操作模块
    QRY_OPERATION_MODULE = (By.XPATH, '//label[contains(text(),"操作模块")]/../div/div/img')
    QRY_OPERATION_MODULE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 操作人员
    QRY_OPERATOR = (By.XPATH, '//label[contains(text(),"操作人员")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
