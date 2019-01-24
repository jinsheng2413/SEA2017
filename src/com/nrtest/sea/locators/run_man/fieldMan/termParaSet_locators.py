# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: termParaSet_locators.py
@time: 2018/11/5 0005 16:29
@desc:
"""

from selenium.webdriver.common.by import By


# 运行管理-现场管理-终端运行参数设置
class TermParaSetLocators:
    # 【查询条件区】
    # 终端地址
    QRY_TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'终端地址\')]/../../div[1]/div[1]//input")
    # 终端厂商
    QRY_TMNL_FACTORY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'终端厂商\')]/../../div[1]/div[1]//img")
    QRY_TMNL_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'上海协同\')]/../div[contains(text(),'%s')]")
    # 规约
    QRY_TMNL_PROTOCOL = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'规约\')]/../../div[1]/div[1]//img")
    QRY_TMNL_PROTOCOL_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'698规约\')]/../div[contains(text(),'%s')]")
    # 任务状态
    QRY_TAST_STATUS = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'任务状态\')]/../div[1]/div[1]//img")
    QRY_TAST_STATUS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'仅保存\')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),\'查询\')])")


# 【js区】

# 【显示区】
TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
