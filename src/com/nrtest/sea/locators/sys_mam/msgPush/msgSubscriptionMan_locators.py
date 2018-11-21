# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: msgSubscriptionMan_locators.py
@time: 2018/11/21 15:56
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→信息定制→推送信息定制→手机订阅→短信订阅管理
class MsgSubscriptionManLocators:
    # 订阅类型
    QRY_SUB_TYPE = (By.XPATH, '//label[contains(text(),"订阅类型")]/../div/div/img')
    QRY_SUB_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发送范围
    QRY_SEND_SCOPE = (By.XPATH, '//label[contains(text(),"发送范围")]/../div/div/img')
    QRY_SEND_SCOPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
