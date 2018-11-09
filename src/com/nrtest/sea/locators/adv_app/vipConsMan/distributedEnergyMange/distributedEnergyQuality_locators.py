# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyQuality_locators.py
@time: 2018/11/9 11:05
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率趋势
class SuccessRateTrendLocators:
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 本地通讯方式
    QRY_COMM_MODE = (By.XPATH, '//input[@id="succRateTrendCommModelCombo"]')
    QRY_COMM_MODE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 远程通讯方式
    QRY_COLL_MODE = (By.XPATH, '//input[@id="succRateTrendCollModelCombo"]')
    QRY_COLL_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@id="succRateTrendAbsoModeCombo"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 发电类型
    QRY_ELEC_TYPE = (By.XPATH, '//input[@id="succRateTrendElecTypeCombox"]')
    QRY_ELEC_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率统计
class SuccessRateStatisticsLocators:
    # 日期
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"日期")]/../div/div/input)[2]')
    # 本地通讯方式
    QRY_COMM_MODE = (By.XPATH, '//input[@id="succRateStatCommModelCombo"]')
    QRY_COMM_MODE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 远程通讯方式
    QRY_COLL_MODE = (By.XPATH, '//input[@id="succRateStatCollModelCombo"]')
    QRY_COLL_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@id="succRateStatAbsoModeCombo"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 发电类型
    QRY_ELEC_TYPE = (By.XPATH, '//input[@id="succRateStatElecTypeCombox"]')
    QRY_ELEC_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[29].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集质量→采集成功率明细
class SuccessRateDetailLocators:
    # 电能表用途
    QRY_METER_PURPOSE = (By.XPATH, '//input[@id="succRateDetailUsageTypeCombox"]')
    QRY_METER_PURPOSE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电类型
    QRY_ELEC_TYPE = (By.XPATH, '//input[@id="succRateDetailElecTypeCombox"]')
    QRY_ELEC_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@id="succRateDetailAbsoModeCombo"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 日期
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"日期")]/../div/div/input)[2]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[33].removeAttribute("readonly");'
