# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyAnomalyAnalysis_locators.py
@time: 2018/11/9 14:50
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→分布式电源管理→分布式电源异常分析
class DistributedEnergyAnomalyAnalysisLocators:
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 发电类型
    QRY_GC_TYPE = (By.XPATH, '//input[@id="genPowerTypeCombox"]')
    QRY_GC_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@id="genAbsoModeCombox"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源异常分析→分布式电源异常情况明细
class DistributedEnergyAnomalyDetailLocators:
    # 日期
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"日期")]/../div/div/input)[2]')
    # 异常类型
    QRY_EXCEPT_TYPE = (By.XPATH, '//input[@id="genExcepTypeCombox"]')
    QRY_EXCEPT_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电类型
    QRY_GC_TYPE = (By.XPATH, '//input[@id="genPowerTypeDetailCombox"]')
    QRY_GC_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@id="genAbsoModeDetailCombox"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[18].removeAttribute("readonly");'
