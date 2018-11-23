# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: customMsgSend_locators.py
@time: 2018/11/21 16:30
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→信息定制→推送信息定制→手机订阅→自定义短信发送
class CustomMsgSendLocators:
    # 单位名称
    QRY_ORG_NAME = (By.XPATH, '//label[contains(text(),"单位名称")]/../div/input')
    # 联系人
    QRY_LINKMAN = (By.XPATH, '//label[contains(text(),"联系人")]/../div/input')
    # 手机号码
    QRY_PHONE_NO = (By.XPATH, '//label[contains(text(),"手机号码")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
