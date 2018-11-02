# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossDetail_locators.py
@time: 2018/11/2 9:20
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→台区线损统计查询→台区线损明细
class TgLineLossDetailLocators:
    # 台区编号
    QRY_TG_NO = (By.XPATH, '//label[contains(text(),"台区编号")]/../div/input')
    # 台区名称
    QRY_TG_NAME = (By.XPATH, '//label[contains(text(),"台区名称")]/../div/input')
    # 查询日期，开始
    QRY_START_DATE = (By.XPATH, '(//label[contains(text(),"日期")]/../div/div/input)[1]')
    # 查询日期，结束
    QRY_END_DATE = (By.XPATH, '(//label[contains(text(),"日期")]/../div/div/input)[2]')
    # 责任人工号
    QRY_CHARGE_PERSON_NO = (By.XPATH, '//label[contains(text(),"责任人工号")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，开始，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[15].removeAttribute("readonly");'
    # 查询日期，结束，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[16].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
