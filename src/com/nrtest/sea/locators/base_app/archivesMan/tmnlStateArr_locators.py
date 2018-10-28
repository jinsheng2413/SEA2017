# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: tmnlStateArr_locators.py
@time: 2018/9/29 0029 11:37
@desc:
'''
from selenium.webdriver.common.by import By


# 基本应用--》档案管理--》终端状态维护
class TmnlStateArrLocators:
    # 【查询条件区】
    # 终端地址
    QRY_TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]//input")
    # 终端状态
    QRY_TMNL_STATUS = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端状态')]/../../div[1]/div[1]//input")
    QRY_TMNL_STATUS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'停运')]/../div[contains(text(),'%s')]")
    # 统计日期
    QRY_COUNT_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'统计日期')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    COUNT_DATE_JS = 'document.getElementById("tmnlStatusStatDate").removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
