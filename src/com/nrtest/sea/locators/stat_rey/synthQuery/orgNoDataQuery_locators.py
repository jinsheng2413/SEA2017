# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: orgNoDataQuery_locators.py
@time: 2018/9/29 15:24
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→供电单位数据查询
class OrgNoDataQueryLocator:
    # 日期
    DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')

    # 【JS属性】
    # 日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '//div[contains(text(),"1027.86%")]')
