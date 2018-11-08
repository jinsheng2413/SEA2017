# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysOtherQuery_locators.py
@time: 2018/11/8 11:07
@desc:
"""
from selenium.webdriver.common.by import By


# 统计查询--》报表管理--》国网报表--》系统其他运行指标
class SysOtherQueryLocators:
    # 【查询条件区】
    #
    QRY_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'日期\')]/../../div[1]/div[1]//input")
    # 统计口径
    QRY_STAT_WAY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'统计口径\')]/../../div[1]/div[1]//input")
    QRY_STAT_WAY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'直供直管\')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById(\'sysOtherDateByDay\').removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
