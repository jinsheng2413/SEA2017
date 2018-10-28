# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterDataQuery_locators.py
@time: 2018/10/9 15:57
@desc:
'''

from selenium.webdriver.common.by import By


# 统计查询→综合查询→抄表数据查询
class MeterDataQueryLocators:
    # 抄表段号
    SECT_NO = (By.XPATH, '//label[contains(text(),"抄表段号")]/../div/input')
    # 电表资产号
    METER_ASSET_NO = (By.XPATH, '//label[contains(text(),"电表资产号")]/../div/input')
    # 用户类型
    CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    # 用户类型→值
    CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 【JS属性】
    # 开始时间，删除readonly属性
    DATE_JS = 'document.getElementById("sendDataQueryDateStart").removeAttribute("readonly");'
