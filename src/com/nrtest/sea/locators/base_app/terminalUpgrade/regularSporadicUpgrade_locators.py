# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: regularSporadicUpgrade_locators.py
@time: 2018/9/26 16:12
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→终端升级→常规零星升级
class RegularSporadicUpgradeLocators:
    # 终端厂家
    TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    # 终端厂家→值
    TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端类型
    TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    # 终端类型→值
    TMNL_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 终端用途
    TMNL_PURPOSE = (By.XPATH, '//label[contains(text(),"终端用途")]/../div/div/img')
    # 终端用途→值
    TMNL_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 升级版本号
    UPGRADE_VERSION_NO = (By.XPATH, '//label[contains(text(),"升级版本号")]/../div/div/img')
    # 升级版本号→值
    UPGRADE_VERSION_NO_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 起始终端地址
    TMNL_ADDR_START = (By.XPATH, '//label[contains(text(),"起始终端地址")]/../div/input')
    # 结束终端地址
    TMNL_ADDR_END = (By.XPATH, '//label[contains(text(),"结束终端地址")]/../div/input')
    # 终端资产号
    TMNL_ASSET_NO = (By.XPATH, '//label[contains(text(),"终端资产号")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 【校验】
    CHECK = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
