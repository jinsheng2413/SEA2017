# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: allCollectSuccessRate_locators.py
@time: 2018/10/16 0016 10:38
@desc:
"""
from selenium.webdriver.common.by import By


class AllCollectSuccessRateLocators:
    # 【查询条件区】
    # 电能表抄表状态
    QRY_METER_READ_STATE = (
        By.XPATH, "//*[@id=\"taskMetStatusComboBox\"]")
    QRY_METER_READ_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'未停抄')]/../div[contains(text(),'%s')]")
    # 终端运行状态
    QRY_TMNL_RUN_STATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端运行状态')]/../../div[1]/div[1]//input)[1]")
    QRY_TMNL_RUN_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'运行')]/../div[contains(text(),'%s')]")
    # 用户编号
    QRY_USER_NO = (By.XPATH, "//*[@id=\"realTimeReadTaskQueryConsNo\"]")
    # 表资产号
    QRY_SURFACE_ASSERT_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'表资产号')]/../../div[1]/div[1]//input")
    QRY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')]")
    # 用户类型
    QRY_USERTYPE = (By.XPATH, "//*[@id=\"taskConsSortCombo\"]")
    QRY_USERTYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//*[contains(text(),\'%s\')]//img")
    #
    QRY_ = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
    # 【JS属性】
    # 采集开始时间，删除readonly属性
    USERTYPE_JS = 'document.getElementById("taskConsSortCombo").removeAttribute("readonly");'
