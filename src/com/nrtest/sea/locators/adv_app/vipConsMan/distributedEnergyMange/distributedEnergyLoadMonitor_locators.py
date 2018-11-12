# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyLoadMonitor_locators.py
@time: 2018/11/12 10:00
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→分布式电源管理→分布式电源负荷监测
class DistributedEnergyLoadMonitorLocators:
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 发电类型
    QRY_ELEC_TYPE = (By.XPATH, '//input[@id="loadMonGenElecTypeCombox"]')
    QRY_ELEC_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@id="genConTypeCombox"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[10].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源负荷监测→分布式电源负荷监测明细
class DistributedEnergyLoadMonitorDetailLocators:
    # 电能表用途
    QRY_METER_PURPOSE = (By.XPATH, '//input[@name="detailUsageType"]')
    QRY_METER_PURPOSE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发电类型
    QRY_ELEC_TYPE = (By.XPATH, '//input[@name="detailGenElecTypeCombox"]')
    QRY_ELEC_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 发电量消纳方式
    QRY_ABSO_MODE = (By.XPATH, '//input[@name="detailGenConTypeCombox"]')
    QRY_ABSO_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 日期
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"日期")])[2]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 开始日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[31].removeAttribute("readonly");'
