# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: onlyChangeSysthesisQuery_locators.py
@time: 2019-02-19 14:00
@desc:
"""
from selenium.webdriver.common.by import By


class LoadDayDataLocators():
    PS_SIDE = (By.XPATH, '//input[@id="any"]/following-sibling::img')
