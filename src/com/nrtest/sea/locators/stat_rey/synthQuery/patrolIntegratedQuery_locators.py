# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: patrolIntegratedQuery_locators.py
@time: 2018/10/19 15:50
@desc:
'''

from selenium.webdriver.common.by import By


# 统计查询→综合查询→巡检仪综合查询
class PatrolIntegratedQueryLocators:
    # 巡检仪运行指标
    # 日期
    DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')
    # 巡检仪运行指标明细
    # 日期
    DETAIL_DATE = (By.XPATH, '(//label[contains(text(),"日期")]/../div/div/input)[2]')
    # 指标
    DETAIL_INDEX = (By.XPATH, '//label[contains(text(),"指标")]/../div/div/img')
    # 指标→值
    DETAIL_INDEX_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端地址
    DETAIL_TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 查询按钮
    BTN_DETAIL_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 【JS属性】
    # 巡检仪运行指标，日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
    # 巡检仪运行指标明细，日期，删除readonly属性
    DETAIL_DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
