# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesGet_locators.py
@time: 2018/11/28 0028 13:51
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用--》档案管理--》电表批量导出（冀北）

class ArchivesGetLocators:
    #【查询条件区】
    #户号
    QRY_USER_NO = (By.XPATH, "//*[@name=\"consNo\"]")
    #用户类型
    QRY_USER_TYPE = (By.XPATH, "//*[@name=\"consTypeCombox\"]")
    QRY_USER_TYPE_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'公变')]/../div[contains(text(),'%s')]")
    #终端资产号
    QRY_TMNL_ASSET_NO = (By.XPATH, "//*[@name=\"tmnlNo\"]")
    #终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")


     
     
     
     
     