# -*- coding:utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: base_locators.py
@time: 2018-12-03 14:37
@desc:
"""
from selenium.webdriver.common.by import By


class BaseLocators:
    QRY_INPUT = (By.XPATH, '//label[text()="{}"]/..//input')

    QRY_DROPDOWN_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[contains(text(),"{}")]')