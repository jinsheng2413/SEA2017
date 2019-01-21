# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: outMemberMan_locators.py
@time: 2018/11/13 0013 10:15
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→采集运维平台→组织运维管理
class OutNameTroopLocators:
    #【查询条件区】
    #外包队伍名称
    QRY_OUT_NAME = (By.XPATH, "//*[@id=\"outName\"]")


    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    #【显示区】
    TAB_ONE = (By.XPATH, '(//*[text()=\'成员明细\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
class OutNameTroopMemberLocators:
    #【查询条件区】
    #外包队伍名称
    QRY_OUT_NAME = (By.XPATH, "//*[@id=\"outNameForMem\"]")


    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")
    #【显示区】
    TAB_ONE = (By.XPATH, '(//*[text()=\'手机\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     