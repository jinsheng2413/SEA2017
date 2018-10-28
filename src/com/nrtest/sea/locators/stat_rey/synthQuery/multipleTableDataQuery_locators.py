# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: multipleTableDataQuery_locators.py
@time: 2018/10/10 15:35
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→多表合一抄表数据查询
class MultipleTableDataQueryLocators:
    # 用户抄表数据
    # 用户编号
    CONS_CONS_NO = (By.XPATH, '//label[contains(text(),"用户编号")]/../div/input')
    # 开始日期
    CONS_START_DATE = (By.XPATH, '//label[contains(text(),"开始日期")]/../div/div/input')
    # 结束日期
    CONS_END_DATE = (By.XPATH, '//label[contains(text(),"结束日期")]/../div/div/input')
    # 用户状态
    CONS_CONS_STATUS = (By.XPATH, '//label[contains(text(),"用户状态")]/../div/div/img')
    # 用户状态→值
    CONS_CONS_STATUS_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')

    # 【JS属性】
    # 开始日期，删除readonly属性
    CONS_START_DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
    # 结束日期，删除readonly属性
    CONS_END_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'
