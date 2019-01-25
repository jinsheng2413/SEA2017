# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterRealTimePowerCutQuery_locators.py
@time: 2018/11/6 15:14
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→配变监测分析→停电分析→表计实时停上电信息查询
class MeterRealTimePowerCutQueryLocators:
    # 台区编号
    QRY_TG_NO = (By.XPATH, '//label[contains(text(),"台区编号")]/../div/input')
    # 用户编号
    QRY_CONS_NO = (By.XPATH, '//label[contains(text(),"用户编号")]/../div/input')
    # 电表资产号
    QRY_METER_ASSET_NO = (By.XPATH, '//label[contains(text(),"电表资产号")]/../div/input')
    # 停电标志
    QRY_POWER_CUT_FLAG = (By.XPATH, '//label[contains(text(),"停电标志")]/../div/div/img')
    QRY_POWER_CUT_FLAG_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
