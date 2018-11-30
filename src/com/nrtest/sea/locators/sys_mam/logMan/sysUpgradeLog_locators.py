# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysUpgradeLog_locators.py
@time: 2018/11/30 10:52
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→日志管理→系统升级日志
class SysUpgradeLogLocators:
    # 版本类型
    QRY_VERSION_TYPE = (By.XPATH, '//label[text()="版本类型"]/../div/div/img')
    QRY_VERSION_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
