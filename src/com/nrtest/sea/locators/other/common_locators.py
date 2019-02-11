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
    POPUP_DLG = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]')
    POPUP_DLG_CONFIRM = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]//button[text()="确定"]')
