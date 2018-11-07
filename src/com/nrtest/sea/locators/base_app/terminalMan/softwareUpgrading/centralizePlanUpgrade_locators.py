# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: centralizePlanUpgrade_locators.py
@time: 2018/9/29 10:41
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→终端管理→软件升级→集中计划升级
class CentralizePlanUpgradeLocators:
    # 集中计划升级
    # 终端厂家
    TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    # 终端厂家→值
    TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 升级目的
    UPGRADE_PURPOSE = (By.XPATH, '//label[contains(text(),"升级目的")]/../div/div/img')
    # 升级目的→值
    UPGRADE_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 终端用途
    TMNL_PURPOSE = (By.XPATH, '//label[contains(text(),"终端用途")]/../div/div/img')
    # 终端用途→值
    TMNL_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 开始时间
    START_DATE = (By.XPATH, '//label[contains(text(),"开始时间")]/../div/div/input')
    # 结束时间
    END_DATE = (By.XPATH, '//label[contains(text(),"结束时间")]/../div/div/input')
    # 批次号
    BATCH_NO = (By.XPATH, '//label[contains(text(),"批次号")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 制定计划
    # 终端厂家
    TAB_TMNL_FACTORY = (By.XPATH, '(//label[contains(text(),"终端厂家")]/../div/div/img)[2]')
    # 终端厂家→值
    TAB_TMNL_FACTORY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 终端类型
    TAB_TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    # 终端类型→值
    TAB_TMNL_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 终端用途
    TAB_TMNL_PURPOSE = (By.XPATH, '(//label[contains(text(),"终端用途")]/../div/div/img)[2]')
    # 终端用途→值
    TAB_TMNL_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[6]/div[%s]')
    # 升级版本号
    TAB_UPGRADE_VERSION_NO = (By.XPATH, '//label[contains(text(),"升级版本号")]/../div/div/input')
    # 升级版本号→值
    TAB_UPGRADE_VERSION_NO_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[7]/div[%s]')
    # 查询按钮
    TAB_BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[2]')

    # 【JS属性】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'
