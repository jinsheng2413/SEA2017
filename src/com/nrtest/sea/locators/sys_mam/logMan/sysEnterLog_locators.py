# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysEnterLog_locators.py
@time: 2018/11/29 13:47
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→日志管理→系统登录日志
class SysEnterLogLocators:
    # 查询日期，开始
    QRY_START_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 查询日期，结束
    QRY_END_DATE = (By.XPATH, '//label[contains(text(),"到")]/../div/div/input')
    # 操作人员
    QRY_OPERATOR = (By.XPATH, '//label[contains(text(),"操作人员")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，开始，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
    # 查询日期，结束，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
