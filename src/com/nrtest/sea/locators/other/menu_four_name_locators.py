# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: menu_four_name_locators.py
@time: 2018/7/19 0019 15:09
@desc:
"""
from selenium.webdriver.common.by import By


class MenuFourNameLocators:
    MONITOR_CUST = (By.XPATH, "(//*[contains(text(),'工作台定制')])[@class=\"x-tab-strip-text GatherQualityEvaluate\"]")
