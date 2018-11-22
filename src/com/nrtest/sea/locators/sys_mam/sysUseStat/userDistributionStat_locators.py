# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userDistributionStat_locators.py
@time: 2018/11/13 14:15
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→系统使用情况统计→用户分布情况统计
# 系统管理→系统使用情况统计→用户分布情况统计→用户分布统计
class UserDistributionStatLocators:
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 系统管理→系统使用情况统计→用户分布情况统计→注册用户明细
class UserRegisterDetailLocators:
    # 类型
    QRY_TYPE = (By.XPATH, '//label[contains(text(),"类型")]/../div/div/img')
    QRY_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
