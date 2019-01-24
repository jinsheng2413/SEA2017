# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: authorityMan_locators.py
@time: 2018/11/23 14:31
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→权限密码管理→权限管理
class AuthorityManLocators:
    # 工号
    QRY_STAFF_NO = (By.XPATH, '//label[contains(text(),"工号")]/../div/input')
    # 用户名
    QRY_STAFF_NAME = (By.XPATH, '//label[contains(text(),"用户名")]/../div/input')
    # 当前状态
    QRY_CUR_STATUS = (By.XPATH, '//label[contains(text(),"当前状态")]/../div/div/img')
    QRY_CUR_STATUS_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
