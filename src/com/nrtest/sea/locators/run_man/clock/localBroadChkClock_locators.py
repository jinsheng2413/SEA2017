# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_locators.py
@time: 2018/11/2 16:11
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→时钟管理→本地广播校时设置
class LocalBroadChkClockLocators:
    # 【查询条件】
    # 节点名称
    NODE = (By.XPATH, ("//div[@class=\"x-form-item \"]//*[contains(text(),'节点名称')]/../div/input"))
    # 终端地址
    TMNL_ADDR = (By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'终端地址')]/../div/input")
    # 终端类型-下拉框
    TMNL_TYPE_SEL = (By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'终端类型')]/../div/div/img")
    # 终端类型
    TMNL_TYPE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'低压集中器')]/../div[contains(text(),'%s')]")
    # 终端厂家-下拉框
    TMNL_FAC_SEL = (By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'终端厂家')]/../div/div/img")
    # 终端厂家
    TMNL_FAC = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'宁波三星')]/../div[contains(text(),'%s')]")
    # 终端规约-下拉框
    TMNL_PROTOCOL_SEL = (By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'终端规约')]/../div/div/img")
    # 终端规约
    TMNL_PROTOCOL = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'698规约')]/../div[contains(text(),'%s')]")
    # 设置状态-下拉框
    SET_STATUS_SEL = (By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'设置状态')]/../div/div/img")
    # 设置状态
    SET_STATUS = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'已设置')]/../div[contains(text(),'%s')]")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')]")

    # 【显示区】
    TABLE_DATA = (By.XPATH, "(//div[@class=\"x-grid3-scroller\"]/div/div)[1]")
