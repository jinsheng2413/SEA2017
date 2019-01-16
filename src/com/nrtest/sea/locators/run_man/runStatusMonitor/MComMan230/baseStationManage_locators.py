# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: baseStationManage_locators.py
@time: 2018/11/6 0006 15:56
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→采集信道管理→230M通信管理→基站信息维护
class BaseStationManageLocators:
    # 【查询条件区】
    # 通信地址
    QRY_COMMUNICATION_ADDR = (By.XPATH,
                              "//*[text()='查询']/ancestor::div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder x-column-layout-ct\"]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
