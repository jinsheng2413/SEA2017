# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: orgVoltageStationSet_locators.py
@time: 2018/11/21 11:08
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→模板管理→供电电压测点设置
class OrgVoltageStationSetLocators:
    # 用户编号
    QRY_CONS_NO = (By.XPATH, '//label[contains(text(),"用户编号")]/../div/input')
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 电表资产
    QRY_METER_ASSET_NO = (By.XPATH, '//label[contains(text(),"电表资产")]/../div/input')
    # 注册信息
    QRY_LOGIN_INFOR = (By.XPATH, '//label[contains(text(),"注册信息")]/../div/div/img')
    QRY_LOGIN_INFOR_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
