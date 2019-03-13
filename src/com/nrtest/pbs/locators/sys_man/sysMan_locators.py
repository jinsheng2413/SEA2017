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

    # 系统管理--部门管理
    # 输入框
    INPUT_NAME1 = (By.XPATH, '/html/body/div[1]/div/div[1]/span/span/input[1]')
    # 查询
    BTN_QUERY1 = (By.XPATH, '/html/body/div[1]/div/div[1]/span/span/span/a')

    # 系统管理--页面管理
    # 输入框
    INPUT_NAME2 = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div/div/div[1]/span/input[1]')
    # 查询
    BTN_QUERY2 = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div/div/div[1]/span/span/a')

    # 系统管理--用户定义
    # 输入框
    INPUT_NAME3 = (By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/span/input[1]')
    # 查询
    BTN_QUERY3 = (By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/span/span/a')
    # 系统管理--用户定义
    # 查询
    BTN_QUERY4 = (By.XPATH, '/html/body/div[1]/div[1]/table/tbody/tr/td[10]/button')
