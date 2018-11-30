# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: menuUseStat_locators.py
@time: 2018/11/30 11:14
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→系统使用情况统计→菜单使用情况统计
class MenuUseStatLocators:
    # 菜单
    QRY_MENU = (By.XPATH, '//label[text()="菜单"]/../div/div/img')
    QRY_MENU_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 操作员
    QRY_OPERATOR = (By.XPATH, '//label[text()="操作员"]/../div/input')
    # 查询日期，开始
    QRY_START_DATE = (By.XPATH, '//label[text()="访问日期"]/../div/div/input')
    # 查询日期，结束
    QRY_END_DATE = (By.XPATH, '//label[text()="到"]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，开始，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'
    # 查询日期，结束，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 系统管理→系统使用情况统计→菜单使用情况统计→菜单使用明细
class MenuUseDetailLocators:
    # 菜单
    QRY_MENU = (By.XPATH, '(//label[text()="菜单"])[2]/../div/div/img')
    QRY_MENU_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 操作员
    QRY_OPERATOR = (By.XPATH, '(//label[text()="操作员"])[2]/../div/input')
    # 查询日期，开始
    QRY_START_DATE = (By.XPATH, '(//label[text()="访问日期"])[2]/../div/div/input')
    # 查询日期，结束
    QRY_END_DATE = (By.XPATH, '(//label[text()="到"])[2]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，开始，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
    # 查询日期，结束，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
