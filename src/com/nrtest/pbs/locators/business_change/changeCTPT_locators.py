# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: changeCTPT_locators.py
@time: 2019-03-13 9:55
@desc:
"""

from selenium.webdriver.common.by import By


# 业务变更→换CT/PT:换CTPT操作
class ChangeCTPTOperateLocators:
    # 查询按钮
    BTN_QUERY = (
        By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/table/tbody/tr[1]/td/button[1]')


# 业务变更→换CT/PT:换CTPT记录
class ChangeCTPTRecordLocators:
    # 查询按钮
    BTN_QUERY = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[1]/button[1]')
