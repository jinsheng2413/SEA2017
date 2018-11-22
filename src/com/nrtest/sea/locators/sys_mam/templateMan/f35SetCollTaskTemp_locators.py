# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: f35SetCollTaskTemp_locators.py
@time: 2018/11/21 15:05
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→模板管理→F35设置采集任务模板
class F35SetCollTaskTempLocators:
    # 任务分类
    QRY_TASK_CLASSIFY = (By.XPATH, '//label[contains(text(),"任务分类")]/../div/div/img')
    QRY_TASK_CLASSIFY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 任务类型
    QRY_TASK_TYPE = (By.XPATH, '//label[contains(text(),"任务类型")]/../div/div/img')
    QRY_TASK_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 模板名称
    QRY_TEMPLATE_NAME = (By.XPATH, '//label[contains(text(),"模板名称")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
