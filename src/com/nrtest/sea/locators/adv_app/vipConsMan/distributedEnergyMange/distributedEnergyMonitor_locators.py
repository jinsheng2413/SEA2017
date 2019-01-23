# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyMonitor_locators.py
@time: 2018/11/8 10:01
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测
# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集监测统计
class DistributedEnergyMonitorStatisticsLocators:
    # 查询日期，开始
    QRY_START_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 查询日期，结束
    QRY_END_DATE = (By.XPATH, '//label[contains(text(),"-")]/../div/div/input')
    # 发电类型
    QRY_ELEC_TYPE = (By.XPATH, '//input[@name="genElecTypeCombox"]')
    QRY_ELEC_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，开始，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
    # 查询日期，结束，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集监测明细
class DistributedEnergyMonitorDetailLocators:
    # 户号
    QRY_CONS_NO = (By.XPATH, '//label[contains(text(),"户号")]/../div/input')
    # 电能表资产编号
    QRY_METER_ASSET_NO = (By.XPATH, '//label[contains(text(),"电能表资产编号")]/../div/input')
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 发电类型
    QRY_ELEC_TYPE = (By.XPATH, '//input[@name="genElecTypeDetailCombox"]')
    QRY_ELEC_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[15].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源采集成功率
class DistributedEnergySuccessRateLocators:
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '//input[@name="readDisSortTypeCombo"]')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'


# 高级应用→重点用户监测→分布式电源管理→分布式电源采集监测→分布式电源用户抄表失败明细
class DistributedEnergyUserFailedLocators:
    # 用户类型
    QRY_CONS_TYPE = (By.XPATH, '//input[@name="disFailListSortTypeCombo"]')
    QRY_CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 电能表资产编号
    QRY_METER_ASSET_NO = (By.XPATH, '//label[contains(text(),"电能表资产编号")]/../div/input')
    # 发电用户编号
    QRY_GC_CONS_NO = (By.XPATH, '//label[contains(text(),"发电用户编号")]/../div/input')
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 查询日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[16].removeAttribute("readonly");'
