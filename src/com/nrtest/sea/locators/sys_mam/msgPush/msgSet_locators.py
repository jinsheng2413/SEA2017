# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: msgSet_locators.py
@time: 2018/11/27 9:55
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→信息定制→推送信息定制→信息设置
class MsgSetLocators:
    # 重要性级别
    QRY_IMPORTANCE_LEVEL = (By.XPATH, '//label[contains(text(),"重要性级别")]/../div/div/img')
    QRY_IMPORTANCE_LEVEL_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
