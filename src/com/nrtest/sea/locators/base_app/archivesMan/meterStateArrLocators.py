# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: meterStateArrLocators.py
@time: 2018/9/26 0026 15:40
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→档案管理→电能表状态维护
class MeterStateArrLocators:
    # 【查询条件区】
    # 筛选条件
    QRY_SCREEN_CONDITION = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'筛选条件')]/../../div[1]/div[1]/div/img")
    QRY_SCREEN_CONDITION_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'用户名称')]/../div[contains(text(),'%s')]")
    QRY_SCREEN_CONDITION_INPUT = (
        By.XPATH, '//*[@id=\"meterConditionTextField\"]')
    # 终端状态
    QRY_TMNL_STATUS = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端状态')]/../../div[1]/div[1]/div/img")
    QRY_TMNL_STATUS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'运行')]/../div[contains(text(),'%s')]")
    # 终端类型
    QRY_TMNLTYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端类型')]/../../div[1]/div[1]/div/img")
    QRY_TMNLTYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'负荷控制终端')]/../div[contains(text(),'%s')]")
    # 终端地址
    QRY_TMNLADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]/input")
    # 筛选条件
    QRY_METER_STATUS = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'电能表状态')]/../../div[1]/div[1]/div/img")
    QRY_METER_STATUS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'停抄')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_TMNL_QRY = (By.XPATH,
                    "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    BTN_METER_QRY = (By.XPATH,
                     "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TABLE_TMNL_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TABLE_METER_ONE = (
        By.XPATH, '(//*[@class=\"x-panel-body x-border-layout-ct\"]//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
