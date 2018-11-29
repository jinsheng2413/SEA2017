# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlParaTemplate_locators.py
@time: 2018/11/26 15:01
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→模板管理→终端参数模板
class TmnlParaTemplateLocators:
    # 终端类型
    QRY_TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    QRY_TMNL_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端规约
    QRY_TMNL_PROTOCOL = (By.XPATH, '//label[contains(text(),"终端规约")]/../div/div/img')
    QRY_TMNL_PROTOCOL_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
