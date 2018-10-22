# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEffectStatistics_locators.py
@time: 2018/9/29 14:11
@desc:
'''

from selenium.webdriver.common.by import By

# 基本应用→终端管理→软件升级→升级效果统计
class UpgradeEffectStatisticsLocators:
#终端升级统计
    # 终端厂家
    TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    # 终端厂家→值
    TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 升级目的
    UPGRADE_PURPOSE = (By.XPATH, '//label[contains(text(),"升级目的")]/../div/div/img')
    # 升级目的→值
    UPGRADE_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

#终端升级明细
    # 终端厂家
    DETAIL_TMNL_FACTORY = (By.XPATH, '(//label[contains(text(),"终端厂家")]/../div/div/img)[2]')
    # 终端厂家→值
    DETAIL_TMNL_FACTORY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 升级目的
    DETAIL_UPGRADE_PURPOSE = (By.XPATH, '(//label[contains(text(),"升级目的")]/../div/div/img)[2]')
    # 升级目的→值
    DETAIL_UPGRADE_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 查询按钮
    BTN_DETAIL_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[2]')
