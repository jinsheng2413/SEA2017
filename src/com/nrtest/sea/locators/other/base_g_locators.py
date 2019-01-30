# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: base_g_locators.py
@time: 2019/1/30 0030 10:57
@desc:
"""
from selenium.webdriver.common.by import By


class BaseTabLocators:
    TREE_TAB_ELE = (By.XPATH, '//div[@id="leftUserGrid"]//div[@class="x-grid3-scroller"]//span[contains(text(),"{}")]')
