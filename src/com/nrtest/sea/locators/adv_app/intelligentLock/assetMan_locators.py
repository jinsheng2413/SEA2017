# -*- coding: utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: assetMan_locators.py
@time: 2018/10/26 13:41
@desc:
'''

from selenium.webdriver.common.by import By

# 高级应用→智能锁具→资产管理


class AssetManLocators:
    # 锁封编号
    LOCK_NO = (By.XPATH, '//label[contains(text(),"锁封编号")]/../div/div/input')
    # 台区名称
    TG_NAME = (By.XPATH, '//label[contains(text(),"台区名称")]/../div/div/input')
    # 用户名称
    USER_NAME = (By.XPATH, '//label[contains(text(),"用户名称")]/../div/div/input')
    # 用户类型
    CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/input')
    # 用户类型→值
    CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 锁封资产状态
    LOCK_ASSET_STATUS = (
        By.XPATH, '//label[contains(text(),"锁封资产状态")]/../div/div/input')
    # 锁封资产状态→值
    LOCK_ASSET_STATUS_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 锁封状态
    LOCK_STATUS = (
        By.XPATH, '//label[contains(text(),"锁封状态")]/../div/div/input')
    # 锁封状态→值
    LOCK_STATUS_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 锁封类型
    LOCK_TYPE = (By.XPATH, '//label[contains(text(),"锁封类型")]/../div/div/input')
    # 锁封类型→值
    LOCK_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
