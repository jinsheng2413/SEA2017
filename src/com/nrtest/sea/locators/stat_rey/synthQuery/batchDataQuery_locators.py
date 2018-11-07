# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: batchDataQuery_locators.py
@time: 2018/9/29 17:49
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→批量数据查询
class BatchDataQueryLocators:
    # 日期
    DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 终端资产号
    TMNL_ASSET_NO = (By.XPATH, '//label[contains(text(),"终端资产号")]/../div/input')
    # 用户类型
    CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    # 用户类型→值
    CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端地址
    TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')

    # 【JS属性】
    # 日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
