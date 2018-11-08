# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: cPSynthQuery_locators.py
@time: 2018/10/20 13:28
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→采集点综合查询
class CPSynthQueryLocators:
    # 终端状态
    TMNL_STATUS = (By.XPATH, '//label[contains(text(),"终端状态")]/../div/div/img')
    # 终端状态→值
    TMNL_STATUS_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 用户范围
    CONS_RANGE = (By.XPATH, '//label[contains(text(),"用户范围")]/../div/div/img')
    # 用户范围→值
    CONS_RANGE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')
