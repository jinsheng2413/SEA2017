# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: common_locators.py
@time: 2019/1/14 0014 9:21
@desc:
"""
from selenium.webdriver.common.by import By


class CommonLocators:
    # 弹框处理
    ERROR_WINDOW_PROCESS = (By.XPATH, '//div[@class=\" x-window x-window-plain x-window-dlg\"]')
    BTN_CONFIRM_LOCATORS = (By.XPATH, "//*[text()='确定']")
