# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: debuggingAccess_locators.py
@time: 2018-10-24 15:40
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→采集建设情况→调试接入情况
class DebuggingAccessLocators:
    # 页面元素
    # 管理方式
    MANAGE_STYLE = (
        By.XPATH, '//label[contains(text(),"管理方式")]/../div/div/input')
    # 管理方式→值
    MANAGE_STYLE_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 装接方式
    INSTALL_MODE = (
        By.XPATH, '//label[contains(text(),"装接方式")]/../div/div/input')
    # 装接方式→值
    INSTALL_MODE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 日期
    DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS操作】
    # 日期，删除readnoly属性
    DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
