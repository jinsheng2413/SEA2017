# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: allEventDistributionRateStatistics_locators.py
@time: 2018/10/18 9:17
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→全事件配置率统计
class AllEventDistributionRateStatisticsLocators:
    # 全事件配置率统计
    # 时间
    DATE = (By.XPATH, '//label[contains(text(),"时间")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')
    # 全事件未配置明细
    # 时间
    DATE_TAB = (By.XPATH, '(//label[contains(text(),"时间")]/../div/div/input)[2]')
    # 终端类型
    TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    # 终端类型→值
    TMNL_TYPE_VALUE = (By.XPATH, '//div[contains(text(),"全部")]/../div[%s]')
    # 查询按钮
    BTN_SEARCH_TAB = (By.XPATH, '(//button[contains(text(),"查询")])[5]')

    # 【JS属性】
    # 全事件配置率统计→时间，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'
    # 全事件未配置明细→时间，删除readonly属性
    DATE_TAB_JS = 'document.getElementsByTagName("input")[10].removeAttribute("readonly");'
