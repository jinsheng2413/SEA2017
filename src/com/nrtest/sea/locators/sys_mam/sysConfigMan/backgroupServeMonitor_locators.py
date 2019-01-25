# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: backgroupServeMonitor_locators.py
@time: 2018/11/19 14:12
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→系统配置管理→后台服务监测
class BackgroupServeMonitorLocators:
    # 查询日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 运行状态
    QRY_RUN_STATUS = (By.XPATH, '//label[contains(text(),"运行状态")]/../div/div/img')
    QRY_RUN_STATUS_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[3].removeAttribute("readonly");'


# 系统管理→系统配置管理→后台服务监测→后台服务监测明细
class BackgroupServeMonitorDetailLocators:
    # Job名称
    QRY_JOB_NAME = (By.XPATH, '//label[contains(text(),"Job名称")]/../div/input')
    # 服务名称
    QRY_SERVICE_NAME = (By.XPATH, '//label[contains(text(),"服务名称")]/../div/input')
    # 查询日期
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"查询日期")])[2]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'
