# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEffectStatistics_locators.py
@time: 2018/9/29 14:11
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→终端管理→软件升级→升级效果统计
class UpgradeEffectStatisticsLocators:
    # 终端升级统计
    # 终端厂家
    TMNL_FACTORY = (By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/img')
    TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 升级目的
    UPGRADE_PURPOSE = (By.XPATH, '//label[contains(text(),"升级目的")]/../div/div/img')
    UPGRADE_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 终端用途
    TMNL_PURPOSE = (By.XPATH, '//label[contains(text(),"终端用途")]/../div/div/img')
    TMNL_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 终端类型
    TMNL_TYPE = (By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/img')
    TMNL_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 升级类型
    UPGRADE_TYPE = (By.XPATH, '//label[contains(text(),"升级类型")]/../div/div/img')
    UPGRADE_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 查询日期，开始
    START_DATE = (By.XPATH, '//div[@id="startDateForEis"]//input')
    # 查询日期，结束
    END_DATE = (By.XPATH, '//div[@id="endDateForEis"]//input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 【JS属性】
    # 查询日期，开始，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
    # 查询日期，结束，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'

    # 终端升级明细
    # 终端厂家
    DETAIL_TMNL_FACTORY = (By.XPATH, '(//label[contains(text(),"终端厂家")]/../div/div/img)[2]')
    DETAIL_TMNL_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 升级目的
    DETAIL_UPGRADE_PURPOSE = (By.XPATH, '(//label[contains(text(),"升级目的")]/../div/div/img)[2]')
    DETAIL_UPGRADE_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 升级类型
    DETAIL_UPGRADE_TYPE = (By.XPATH, '(//label[contains(text(),"升级类型")]/../div/div/img)[2]')
    DETAIL_UPGRADE_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 终端用途
    DETAIL_TMNL_PURPOSE = (By.XPATH, '(//label[contains(text(),"终端用途")]/../div/div/img)[2]')
    DETAIL_TMNL_PURPOSE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 是否成功
    DETAIL_WHETHER_SUCCESS = (By.XPATH, '//label[contains(text(),"是否成功")]/../div/div/img')
    DETAIL_WHETHER_SUCCESS_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 终端类型
    DETAIL_TMNL_TYPE = (By.XPATH, '(//label[contains(text(),"终端类型")]/../div/div/img)[2]')
    DETAIL_TMNL_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[6]/div[%s]')
    # 升级状态
    DETAIL_UPGRADE_STATUS = (By.XPATH, '//label[contains(text(),"升级状态")]/../div/div/img')
    DETAIL_UPGRADE_STATUS_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[7]/div[%s]')
    # 确认状态
    DETAIL_AFFIRM_STATUS = (By.XPATH, '//label[text()="确认状态"]/../div/div/img')
    DETAIL_AFFIRM_STATUS_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[8]/div[%s]')
    # 确认结果
    DETAIL_AFFIRM_RESULT = (By.XPATH, '//label[text()="确认结果"]/../div/div/img')
    DETAIL_AFFIRM_RESULT_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[9]/div[%s]')
    # 执行开始日期
    DETAIL_START_DATE = (By.XPATH, '//label[text()="执行开始日期"]/../div/div/input')
    # 执行结束日期
    DETAIL_END_DATE = (By.XPATH, '//label[text()="执行结束日期"]/../div/div/input')
    # 确认开始日期
    AFFIRM_START_DATE = (By.XPATH, '//label[text()="确认开始日期"]/../div/div/input')
    # 确认结束日期
    AFFIRM_END_DATE = (By.XPATH, '//label[text()="确认结束日期"]/../div/div/input')
    # 查询按钮
    BTN_DETAIL_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')
    # 执行日期
    BOX_EXECUTE_DATE = (By.NAME, 'execDateStatus')
    # 确认日期
    BOX_AFFIRM_DATE = (By.NAME, 'confirmDateStatus')

    # 【JS属性】
    # 执行开始日期，删除readonly属性
    DETAIL_START_DATE_JS = 'document.getElementsByTagName("input")[30].removeAttribute("readonly");'
    # 执行结束日期，删除readonly属性
    DETAIL_END_DATE_JS = 'document.getElementsByTagName("input")[31].removeAttribute("readonly");'
    # 确认开始日期，删除readonly属性
    AFFIRM_START_DATE_JS = 'document.getElementsByTagName("input")[33].removeAttribute("readonly");'
    # 确认结束日期，删除readonly属性
    AFFIRM_END_DATE_JS = 'document.getElementsByTagName("input")[34].removeAttribute("readonly");'
