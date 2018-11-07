# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: indexAllocation_locators.py
@time: 2018/11/2 13:55
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→同期线损→指标配置
class IndexAllocationLocators:
    # 台区编号
    QRY_TG_NO = (By.XPATH, '//label[contains(text(),"台区编号")]/../div/input')
    # 台区状态
    QRY_TG_STATUS = (
        By.XPATH, '//label[contains(text(),"台区状态")]/../div/div/img')
    QRY_TG_STATUS_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 责任人工号
    QRY_CHARGE_PERSON_NO = (
        By.XPATH, '//label[contains(text(),"责任人工号")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
