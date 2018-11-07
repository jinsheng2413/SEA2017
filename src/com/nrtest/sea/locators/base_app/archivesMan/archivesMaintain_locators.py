# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesMaintain_locators.py
@time: 2018/8/30 0030 14:43
@desc:
"""
from selenium.webdriver.common.by import By


# 档案维护
class ArchivesMaintain_locators:
    # 【菜单】
    # 厂站维护
    BTN_MENU_FACTORY_MAINTAIN = (
        By.XPATH, "(//*[contains(text(),'厂站维护')])[@class=\"x-tab-strip-text \"]")
    # 终端维护
    BTN_MENU_TERMINAL_MAINTAIN = (
        By.XPATH, "(//*[contains(text(),'终端维护')])[@class=\"x-tab-strip-text \"]")
    # 电表维护
    BTN_MENU_METER_MAINTAIN = (
        By.XPATH, "(//*[contains(text(),'电表维护')])[@class=\"x-tab-strip-text \"]")
    # 【查询名称】
    # 厂站名称
    QRY_FACTORY_NAME = (
        By.XPATH, "//*[@class=\"x-form-item \"]//*[contains(text(),'厂站名称')]/../div[1]/div/img")
    QRY_FACTORY_NAME_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'--全部--')]/../div[%s]")
    # 电压等级
    QRY_ELE_GRADE = (
        By.XPATH, "//*[@class=\"x-form-item \"]//*[contains(text(),'电压等级')]/../div[1]/div/img")
    QRY_ELE_GRADE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'--全部--')]/../div[%s]")

    # 终端资产号
    QRY_TERMINAL_ASSET_NO = (By.XPATH,
                             "//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'终端资产号')]/../div/input")
    # 终端地址
    QRY_TERMINAL_ADDR = (By.XPATH,
                         "//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'终端地址')]/../div/input")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')

    # 【操作区】
    BTN_FACTORY_QRY = (By.XPATH, "(//button[contains(text(),'查询')])[1]")
    BTN_TERMINAL_QRY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")
    BTN_METER_QRY = (By.XPATH,
                     "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder x-column-layout-ct\"]//button[contains(text(),'查询')])[2]")
