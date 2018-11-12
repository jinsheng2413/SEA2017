# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: unControlPlantStat_locators.py
@time: 2018/11/12 11:02
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→非统调电厂管理→非统调电厂接入统计
class UnControlPlantStatLocators:
    # 发电方式
    QRY_ELEC_WAY = (By.XPATH, '//input[@id="unGenElecTypeCombox"]')
    QRY_ELEC_WAY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 采集方式
    QRY_GATHER_WAY = (By.XPATH, "//input[@id='unCommModelCombo']")
    QRY_GATHER_WAY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 统计日期
    QRY_DATE = (By.XPATH, '//label[contains(text(),"统计日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'


# 高级应用→重点用户监测→非统调电厂管理→非统调电厂接入统计→非统调电厂接入明细
class UnControlPlantDetailLocators:
    # 发电方式
    QRY_ELEC_WAY = (By.XPATH, '//input[@id="unGenElecTypeDetCombox"]')
    QRY_ELEC_WAY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 采集方式
    QRY_GATHER_WAY = (By.XPATH, "//input[@id='unCommModelDetCombo']")
    QRY_GATHER_WAY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 统计日期
    QRY_DATE = (By.XPATH, '(//label[contains(text(),"统计日期")])[2]/../div/div/input')
    # 户号
    QRY_CONS_NO = (By.XPATH, '//label[contains(text(),"户号")]/../div/input')
    # 表资产编号
    QRY_METER_ASSET_NO = (By.XPATH, '//label[contains(text(),"表资产编号")]/../div/input')
    # 终端资产号
    QRY_TMNL_ASSET_NO = (By.XPATH, '//label[contains(text(),"终端资产号")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
