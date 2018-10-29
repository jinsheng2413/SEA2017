# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: blackListQuery_locators.py
@time: 2018/10/20 14:41
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→黑名单查询
class BlackListQueryLocators:
    # 用户编号
    CONS_NO = (By.XPATH, '//label[contains(text(),"用户编号")]/../div/input')
    # 查询日期
    DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 终端地址
    TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')

    # 【JS属性】
    # 开始日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'
