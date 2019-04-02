# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: collHitch_locators.py
@time: 2019/3/15 14:18
@desc:
"""
from selenium.webdriver.common.by import By


# 档案管理--采集点挂接

class CollHitch_locators:
    # 输入框
    INPUT_NAME = (By.XPATH, '//input[@placeholder="请输入采集点名称..."]')
