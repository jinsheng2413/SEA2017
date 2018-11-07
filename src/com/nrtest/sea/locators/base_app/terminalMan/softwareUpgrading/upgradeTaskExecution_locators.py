# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeTaskExecution_locators.py
@time: 2018/9/28 14:11
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→终端管理→软件升级→升级任务执行
class UpgradeTaskExecutionLocators:
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
    # 开始时间
    START_DATE = (By.XPATH, '//label[contains(text(),"开始时间")]/../div/div/input')
    # 结束时间
    END_DATE = (By.XPATH, '//label[contains(text(),"结束时间")]/../div/div/input')
    # 批次号
    BATCH_NO = (By.XPATH, '//label[contains(text(),"批次号")]/../div/input')
    # 升级目的
    UPGRADE_PURPOSE = (By.XPATH, '//label[contains(text(),"升级目的")]/../div/div/img')
    # 升级目的→值
    UPGRADE_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 升级类型
    UPGRADE_TYPE = (By.XPATH, '//label[contains(text(),"升级类型")]/../div/div/img')
    # 升级类型→值
    UPGRADE_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 执行状态
    EXECUTION_STATE = (By.XPATH, '//label[contains(text(),"执行状态")]/../div/div/img')
    # 执行状态→值
    EXECUTION_STATE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[6]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 【JS属性】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'
