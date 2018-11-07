# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: allEventMeterEventQuery_locators.py
@time: 2018/9/30 14:20
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→全事件电表事件查询
class AllEventMeterEventQueryLocators:
    # 电表资产号
    METER_ASSET_NO = (By.XPATH, '//label[contains(text(),"电表资产号")]/../div/input')
    # 事件等级
    EVENT_LEVEL = (By.XPATH, '//label[contains(text(),"事件等级")]/../div/div/img')
    # 事件等级→值
    EVENT_LEVEL_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 事件类型
    EVENT_TYPE = (By.XPATH, '//label[contains(text(),"事件类型")]/../div/div/img')
    # 事件类型→值
    EVENT_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 采集开始时间
    START_DATE = (By.XPATH, '//label[contains(text(),"采集开始时间")]/../div/div/input')
    # 采集结束时间
    END_DATE = (By.XPATH, '//label[contains(text(),"采集结束时间")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')

    # 【JS属性】
    # 采集开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
    # 采集结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'
