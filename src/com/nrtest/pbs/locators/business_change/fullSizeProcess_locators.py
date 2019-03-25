# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: fullSizeProcess_locators.py
@time: 2019-03-11 14:31
@desc:
"""

from selenium.webdriver.common.by import By


# 业务变更→满码处理:满码处理操作
class FullSizeProcessOperateLocators:
    # 查询按钮
    BTN_QUERY = (By.ID, 'searchhandlebutton')


# 业务变更→满码处理:满码记录查询
class FullSizeProcessRecordLocators:
    # 查询按钮
    BTN_QUERY = (By.ID, 'searchrecordbutton')


# 业务变更→满码处理:满码处理查询
class FullSizeProcessQryLocators:
    # 查询按钮
    BTN_QUERY = (By.ID, 'searchhadlebutton')
