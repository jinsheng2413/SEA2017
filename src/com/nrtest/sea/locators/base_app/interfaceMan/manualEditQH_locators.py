# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: manualEditQH_locators.py
@time: 2018-11-07 16:27
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用--》接口管理--》人工补录（青海）
class ManualEditQH_Locators:
    # 【查询条件区】
    # 抄表段号
    QRY_METER_READING_PARAGRAPH = (By.XPATH, "//label[contains(text(),'抄表段号')]/../div/input")
    # 用户编号
    QRY_CONS_NO = (By.XPATH, "//label[contains(text(),'用户编号')]/../div/input")
    # 数据来源
    QRY_DATA_FROM = (By.XPATH, "//label[contains(text(),'数据来源')]/../div/div/input")
    # 值（数据来源）
    QRY_DATA_FROM_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'%s')]")
    # 日期
    QRY_DATE = (By.XPATH, "(//label[contains(text(),'日期')]/../div/div/input)[1]")
    # 正向有功总为空
    QRY_IS_EMPTY = (By.XPATH, "//label[contains(text(),'正向有功总为空')]")

    # 【操作区】
    BTN_QRY = (By.XPATH, "//*[text()='查询']")

    # 【js区】
    # 开始时间，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
