# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: whiteListQuery_locators.py
@time: 2018/10/19 14:34
@desc:
'''

from selenium.webdriver.common.by import By


# 统计查询→综合查询→白名单查询
class WhiteListQueryLocators:
    # 用户编号
    CONS_NO = (By.XPATH, '//label[contains(text(),"用户编号")]/../div/input')
    # 开始日期
    START_DATE = (By.XPATH, '//label[contains(text(),"开始日期")]/../div/div/input')
    # 结束日期
    END_DATE = (By.XPATH, '//label[contains(text(),"结束日期")]/../div/div/input')
    # 终端地址
    TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')
    # 【JS属性】
    # 开始日期，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'
    # 结束日期，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
