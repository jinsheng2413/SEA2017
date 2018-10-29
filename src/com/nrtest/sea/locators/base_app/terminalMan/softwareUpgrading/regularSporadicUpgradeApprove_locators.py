# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: regularSporadicUpgradeApprove_locators.py
@time: 2018/9/28 9:14
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→终端管理→软件升级→常规零星升级审批
class RegularSporadicUpgradeApproveLocator:
    # 终端厂家
    TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    # 终端厂家→值
    TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 申请状态
    APPLY_STATUS = (By.XPATH, '//input[@name="applyStatusUpgradeCombox"]')
    # 申请状态→值
    APPLY_STATUS_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 终端用途
    TMNL_PURPOSE = (By.XPATH, '//label[contains(text(),"终端用途")]/../div/div/img')
    # 终端用途→值
    TMNL_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 申请开始日期
    START_DATE = (By.XPATH, '//label[contains(text(),"申请开始日期")]/../div/div/input')
    # 申请结束日期
    END_DATE = (By.XPATH, '//label[contains(text(),"申请结束日期")]/../div/div/input')
    # 批次号
    BATCH_NO = (By.XPATH, '//label[contains(text(),"批次号")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 【JS属性】
    # 申请开始日期，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
    # 申请结束日期，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[8].removeAttribute("readonly");'
