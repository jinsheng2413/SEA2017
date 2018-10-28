# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sectDataQuery_locators.py
@time: 2018/9/29 15:59
@desc:
'''

from selenium.webdriver.common.by import By


# 统计查询→综合查询→抄表段数据查询
class SectDataQueryLocators:
    # 抄表段编号
    SECT_NO = (By.XPATH, '//input[@id="mrSectNoForQuery"]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')
    # 数据展示
    # 查询按钮
    BTN_TAB_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[5]')
