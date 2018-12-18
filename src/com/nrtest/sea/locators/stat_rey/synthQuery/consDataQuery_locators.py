# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: consDataQuery_locators.py
@time: 2018/12/12 16:03
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→用户数据查询
class ConsDataQueryLocators:
    # 用户编号
    QRY_CONS_NO = (By.XPATH, '(//label[text()="用户编号"]/../div/input)[1]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
