# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkPointDataRtu_locators.py
@time: 2018/10/31 0031 9:10
@desc:
"""
from selenium.webdriver.common.by import By


# 高级应用-->台线系统--》资料维护--》专变考核点资料维护
class CheckPointDataRtuLocators:
    # 【查询条件区】
    # 抄表段号
    QRY_READ_NO = (By.XPATH, "//*[@id=\"mrSectNoRtu\"]")
    QRY_READ_NO_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'1')]/../div[contains(text(),'%s')]")
    # 用户编号
    QRY_USER_NO = (By.XPATH, "//*[@id=\"rtuCpNo\"]")
    QRY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')]")
    # 用户名称
    QRY_USER_NAME = (By.XPATH, "//*[@id=\"rtuCpName\"]")
    # 电表正反向
    QRY_METER_FR = (By.XPATH, "//*[@id=\"meterzfxRtu\"]")
    QRY_METER_FR_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'正')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
