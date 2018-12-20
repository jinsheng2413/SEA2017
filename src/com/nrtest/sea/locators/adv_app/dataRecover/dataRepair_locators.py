# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: dataRepair_locators.py
@time: 2018-10-31 13:56
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用--》数据修复--》修复数据查询
# 第一个tab页
class DataRepair_1Locators:
    # [显示区]
    # 用户类型
    QRY_CONS_SORT = (
        By.XPATH, "(//label[contains(text(),'用户类型')]/../div/div/input)[1]")
    # 执行状态的值(用户类型)
    QRY_CONS_SORT_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'其它')])[1]/../div[contains(text(),'%s')]")
    # 数据类型
    QRY_DATA_TYPE = (
        By.XPATH, "(//label[contains(text(),'数据类型')]/../div/div/input)[1]")
    # 执行状态的值（数据类型）
    QRY_DATA_TYPE_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'电量')])[1]/../div[contains(text(),'%s')]")
    # 开始日期
    QRY_START_DATE = (
        By.XPATH, "//label[contains(text(),'开始日期')]/../div/div/input")
    # 结束日期
    QRY_END_DATE = (
        By.XPATH, "//label[contains(text(),'结束日期')]/../div/div/input")

    # [操作区]
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'


# 第二个tab页
class DataRepair_2Locators:
    # [显示区]
    # 供电单位
    QRY_ORG = (By.XPATH, "(//label[contains(text(),'供电单位')]/../div/input)[2]")
    # 数据类型
    QRY_DATA_TYPE = (
        By.XPATH, "(//label[contains(text(),'数据类型')]/../div/div/input)[2]")
    # 执行状态的值（数据类型）
    QRY_DATA_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'电量')]/../div[contains(text(),'%s')]")
    # 用户类型
    QRY_CONS_SORT = (
        By.XPATH, "(//label[contains(text(),'用户类型')]/../div/div/input)[2]")
    # 执行状态的值(用户类型)
    QRY_CONS_SORT_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'其它')]/../div[contains(text(),'%s')]")
    # 用户编号
    QRY_CONS_NO = (By.XPATH, "//label[contains(text(),'用户编号')]/../div/input")
    # 终端资产号
    QRY_TMNL_ASST_NO = (
        By.XPATH, "//label[contains(text(),'终端资产号')]/../div/input")
    # 电表局编号
    QRY_METER_NO = (By.XPATH, "//label[contains(text(),'电表局编号')]/../div/input")
    # 查询日期
    QRY_DATE = (By.XPATH, "//label[contains(text(),'查询日期')]/../div/div/input")

    # [操作区]
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[3]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[2]")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[15].removeAttribute("readonly");'
