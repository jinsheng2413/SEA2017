# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyElectricMonitor_locators.py
@time: 2018/11/9 16:34
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→分布式电源管理→分布式电源电量监测→分布式电源电量趋势
class DistributedEnergyElectricTrendLocators:
    # 月份
    QRY_DATE = (By.XPATH, '//label[contains(text(),"月份")]/../div/div/input')
    # 发电类型
    QRY_GC_TYPE = (By.XPATH, '//input[@name="genElecTypeCombox"]')
    QRY_GC_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@name="elecMonElecXnTypeCombox"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源电量监测→分布式电源电量监测统计
class DistributedEnergyElectricStatLocators:
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 发电类型
    QRY_GC_TYPE = (By.XPATH, '//input[@name="monStatElecTypeCombox"]')
    QRY_GC_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@name="monStatElecXnTypeCombox"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源电量监测→分布式电源电量监测明细
class DistributedEnergyElectricDetailLocators:
    # 电能表用途
    QRY_METER_PURPOSE = (By.XPATH, '//input[@name="monDetailMeterUsageCombox"]')
    QRY_METER_PURPOSE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@name="monDetailElecXnTypeCombox"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 发电类型
    QRY_GC_TYPE = (By.XPATH, '//input[@name="monDetailElecTypeCombox"]')
    QRY_GC_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[17].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源电量监测→分布式电源抄表示数查询
class DistributedEnergyQueryLocators:
    # 电能表用途
    QRY_METER_PURPOSE = (By.XPATH, '//input[@name="meterReadUsageTypeCodeCombox"]')
    QRY_METER_PURPOSE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电类型
    QRY_GC_TYPE = (By.XPATH, '//input[@name="meterReadElecTypeCombox"]')
    QRY_GC_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@name="meterReadElecXnTypeCombox"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 开始日期
    QRY_START_DATE = (By.XPATH, '//label[contains(text(),"开始日期")]/../div/div/input')
    # 结束日期
    QRY_END_DATE = (By.XPATH, '//label[contains(text(),"结束日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 开始日期，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[15].removeAttribute("readonly");'
    # 结束日期，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[16].removeAttribute("readonly");'
