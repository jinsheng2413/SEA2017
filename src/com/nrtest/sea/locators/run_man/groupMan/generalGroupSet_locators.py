# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: generalGroupSet_locators.py
@time: 2018/11/12 14:23
@desc:
"""

from selenium.webdriver.common.by import By


# 运行管理→群组管理→普通群组设置
class GeneralGroupSetLocators:
    # 名称
    QRY_NAME = (By.XPATH, '//label[contains(text(),"名称")]/../div/input')

    # 查询日期
    QRY_VALID_DATE = (By.XPATH, '//input[@type="checkbox"]')
    # 开始
    QRY_START_DATE = (By.XPATH, '//label[contains(text(),"有效日期")]/../div/div/input')
    # 查询日期，结束
    QRY_END_DATE = (By.XPATH, '//label[contains(text(),"至")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[12].removeAttribute("readonly");'
    # 查询日期，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//div[@class="x-grid3-cell-inner x-grid3-col-numberer"])[1]')
