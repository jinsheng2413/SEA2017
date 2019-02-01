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

    # 专公变综合查询--》负荷日数据：下拉选择按钮
    RECHARGE_TIME = (
    By.XPATH, '((//label[text()="任意时段"]/ancestor::div[@class=" x-panel x-panel-noborder x-border-panel"])[3]//img)[2]')
    RECHARGE_TIME_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[text()="%s"]')
