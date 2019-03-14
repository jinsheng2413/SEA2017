# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: changeTableOperate_locators.py
@time: 2019-03-08 15:46
@desc:
"""

from selenium.webdriver.common.by import By


# 业务变更→换表操作
class ChangeTableOperateLocators:
    # 查询按钮
    BTN_QUERY = (By.ID, 'confirm')
