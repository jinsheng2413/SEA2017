# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysParameterMan_locators.py
@time: 2018/11/16 10:33
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→系统配置管理→系统参数管理
# 系统管理→系统配置管理→系统参数管理→系统基本参数设置
class SysBasicParaSetLocators:
    # 参数名称
    QRY_PARA_NAME = (By.XPATH, '//label[contains(text(),"参数名称")]/../div/div/img')
    QRY_PARA_NAME_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 参数编码
    QRY_PARA_NO = (By.XPATH, '//label[contains(text(),"参数编码")]/../div/input')
    # 参数项名称
    QRY_PARA_ITEM_NAME = (By.XPATH, '//label[contains(text(),"参数项名称")]/../div/input')
    # 参数项编码
    QRY_PARA_ITEM_NO = (By.XPATH, '//label[contains(text(),"参数项编码")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')


# 系统管理→系统配置管理→系统参数管理→系统异常参数设置
class SysAbnormalParaSetLocators:
    # 参数名称
    QRY_PARA_NAME = (By.XPATH, '(//label[contains(text(),"参数名称")])[2]/../div/div/img')
    QRY_PARA_NAME_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 参数编码
    QRY_PARA_NO = (By.XPATH, '(//label[contains(text(),"参数编码")])[2]/../div/input')
    # 参数项名称
    QRY_PARA_ITEM_NAME = (By.XPATH, '(//label[contains(text(),"参数项名称")])[2]/../div/input')
    # 参数项编码
    QRY_PARA_ITEM_NO = (By.XPATH, '(//label[contains(text(),"参数项编码")])[2]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//div[@class="x-grid3-body"])[2]/div[1]')
