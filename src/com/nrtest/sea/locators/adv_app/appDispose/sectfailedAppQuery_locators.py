# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sectfailedAppQuery_locators.py
@time: 2018/10/29 11:12
@desc:
"""

from selenium.webdriver.common.by import By

# 高级应用→工单处理→抄表失败工单查询


class SectfailedAppQueryLocators:
    # 抄表段号
    SECT_NO = (By.XPATH, '//label[contains(text(),"抄表段号")]/../div/input')
    # 抄表管理员工号
    SECT_MANAGER_NO = (
        By.XPATH, '//label[contains(text(),"抄表管理员工号")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
