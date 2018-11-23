# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: roleMan_locators.py
@time: 2018/11/23 11:28
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→权限密码管理→角色管理
class RoleMAnLocators:
    # 角色名称
    QRY_ROLE_NAME = (By.XPATH, '//label[contains(text(),"角色名称")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
