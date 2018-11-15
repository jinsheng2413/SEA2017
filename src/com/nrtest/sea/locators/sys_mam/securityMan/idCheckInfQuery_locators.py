# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: idCheckInfQuery_locators.py
@time: 2018/11/15 10:33
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→权限密码管理→账号审核信息查询
class IdCheckInfQueryLocators:
    # 审核开始日期
    QRY_START_DATE = (By.XPATH, '//label[contains(text(),"审核开始日期")]/../div/div/input')
    # 审核结束日期
    QRY_END_DATE = (By.XPATH, '//label[contains(text(),"审核结束日期")]/../div/div/input')
    # 审核结果
    QRY_RESULT = (By.XPATH, '//label[contains(text(),"审核结果")]/../div/div/img')
    QRY_RESULT_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 审核开始日期，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[3].removeAttribute("readonly");'
    # 审核结束日期，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
