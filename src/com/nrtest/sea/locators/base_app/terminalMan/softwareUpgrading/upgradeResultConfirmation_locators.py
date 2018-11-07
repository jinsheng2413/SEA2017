# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeResultConfirmation_locators.py
@time: 2018/9/29 9:25
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→终端管理→软件升级→升级结果确认
class UpgradeResultConfirmationLocator:
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
    # 确认开始日期
    START_DATE = (By.XPATH, '//label[contains(text(),"确认开始日期")]/../div/div/input')
    # 确认结束日期
    END_DATE = (By.XPATH, '//label[contains(text(),"确认结束日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 【JS属性】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[11].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[12].removeAttribute("readonly");'
