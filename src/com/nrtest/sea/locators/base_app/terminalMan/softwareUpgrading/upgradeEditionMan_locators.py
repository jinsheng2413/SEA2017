# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEditionMan_locators.py
@time: 2018/9/25 16:09
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→终端管理→软件升级→升级版本管理
class UpgradeEditionManLocators:
    # 终端版本信息登记
    # 终端厂家
    TMNL_FACTORY = (
        By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    # 终端厂家→值
    TMNL_FACTORY_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端类型
    TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    # 终端类型→值
    TMNL_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 终端用途
    TMNL_PURPOSE = (
        By.XPATH, '//label[contains(text(),"终端用途")]/../div/div/img')
    # 终端用途→值
    TMNL_PURPOSE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 软件版本号
    SOFTWARE_VERSION_NO = (
        By.XPATH, '//label[contains(text(),"软件版本号")]/../div/div/img')
    # 软件版本号→值
    SOFTWARE_VERSION_NO_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 升级版本管理
    # 终端厂家
    UPGRADE_TMNL_FACTORY = (
        By.XPATH, '(//label[contains(text(),"终端厂家")]/../div/div/img)[2]')
    # 终端厂家→值
    UPGRADE_TMNL_FACTORY_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 终端类型
    UPGRADE_TMNL_TYPE = (
        By.XPATH, '(//label[contains(text(),"终端类型")]/../div/div/img)[2]')
    # 终端类型→值
    UPGRADE_TMNL_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 终端用途
    UPGRADE_TMNL_PURPOSE = (
        By.XPATH, '(//label[contains(text(),"终端用途")]/../div/div/img)[2]')
    # 终端用途→值
    UPGRADE_TMNL_PURPOSE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[6]/div[%s]')
    # 申请状态
    UPGRADE_APPLY_STATUS = (
        By.XPATH, '//input[@name="applyStatusUpgradeCombox"]')
    # 申请状态→值
    UPGRADE_APPLY_STATUS_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[7]/div[%s]')
    # 申请开始日期
    UPGRADE_START_DATE = (
        By.XPATH, '//label[contains(text(),"申请开始日期")]/../div/div/input')
    # 申请结束日期
    UPGRADE_END_DATE = (
        By.XPATH, '//label[contains(text(),"申请结束日期")]/../div/div/input')
    # 查询按钮
    BTN_UPGRADE_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[2]')

    # 终端版本召测
    # 终端厂家
    EDITION_TMNL_FACTORY = (
        By.XPATH, '(//label[contains(text(),"终端厂家")]/../div/div/img)[3]')
    # 终端厂家→值
    EDITION_TMNL_FACTORY_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[8]/div[%s]')
    # 终端类型
    EDITION_TMNL_TYPE = (
        By.XPATH, '(//label[contains(text(),"终端类型")]/../div/div/img)[3]')
    # 终端类型→值
    EDITION_TMNL_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[9]/div[%s]')
    # 终端用途
    EDITION_TMNL_PURPOSE = (
        By.XPATH, '(//label[contains(text(),"终端用途")]/../div/div/img)[3]')
    # 终端用途→值
    EDITION_TMNL_PURPOSE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[10]/div[%s]')
    # 终端规约
    EDITION_TMNL_PROTOCOL = (
        By.XPATH, '//label[contains(text(),"终端规约")]/../div/div/img')
    # 终端规约→值
    EDITION_TMNL_PROTOCOL_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[11]/div[%s]')
    # 终端地址
    EDITION_TMNL_ADDR = (
        By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 查询按钮
    BTN_EDITION_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[3]')

    # 【JS属性】
    # 申请开始日期，删除readonly属性
    UPGRADE_START_DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
    # 申请结束日期，删除readonly属性
    UPGRADE_END_DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'

    # 【校验区】
    # 终端版本信息登记，校验
    CHECK = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
    # 升级版本管理，校验
    UPGRADE_CHECK = (By.XPATH, '//a[contains(text(),"文件下载")]')
    # 终端版本召测，校验
    EDITION_CHECK = (By.XPATH, '(//font[contains(text(),"离线")])[1]')
