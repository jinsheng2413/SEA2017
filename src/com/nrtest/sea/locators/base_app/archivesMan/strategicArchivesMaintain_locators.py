# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: strategicArchivesMaintain_locators.py
@time: 2018/9/26 0026 14:49
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用--》档案管理--》巡检仪档案管理
class StrategicArchivesMaintainLocators:
    # 【查询条件区】
    # 终端地址
    QRY_TMNLADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]/input")
    # 终端资产号
    QRY_TMNLNO = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端资产号')]/../../div[1]/div[1]/input")
    # 用户编号
    QRY_USERNO = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户编号')]/../../div[1]/div[1]/input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
