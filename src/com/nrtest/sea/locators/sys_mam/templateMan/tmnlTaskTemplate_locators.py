# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlTaskTemplate_locators.py
@time: 2018/11/21 14:33
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→模板管理→终端任务模板
class TmnlTaskTemplateLocators:
    # 任务状态
    QRY_TASK_STAT = (By.XPATH, '//label[contains(text(),"任务状态")]/../div/div/img')
    QRY_TASK_STAT_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 方案类型
    QRY_SCHEME_TYPE = (By.XPATH, '//label[contains(text(),"方案类型")]/../div/div/img')
    QRY_SCHEME_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 执行优先级
    QRY_EXECUTION_PRIORITY = (By.XPATH, '//label[contains(text(),"执行优先级")]/../div/div/img')
    QRY_EXECUTION_PRIORITY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
