# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: countServeDeploy_locators.py
@time: 2018/11/16 16:08
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→系统配置管理→计算服务配置
class CountServeDeployLocators:
    # JOB名称
    QRY_JOB_NAME = (By.XPATH, '//label[contains(text(),"JOB名称")]/../div/div/img')
    QRY_JOB_NAME_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 服务名称
    QRY_SERVICE_NAME = (By.XPATH, '//label[contains(text(),"服务名称")]/../div/div/img')
    QRY_SERVICE_NAME_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
