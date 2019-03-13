# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: sysMan_locators.py
@time: 2019/3/13 10:45
@desc:
"""

from selenium.webdriver.common.by import By


class SysMan_locators:
    # 系统管理--系统菜单

    # 输入框
    INPUT_NAME = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/span/input[1]')
    # 查询
    BTN_QUERY = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/span/span/a')
