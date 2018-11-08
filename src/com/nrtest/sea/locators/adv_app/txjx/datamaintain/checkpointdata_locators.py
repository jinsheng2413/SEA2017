# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkpointdata_locators.py
@time: 2018/10/30 0030 17:15
@desc:
"""
from selenium.webdriver.common.by import By

# 高级应用-->台线系统--》资料维护--》线路考核点资料维护


class CheckpointdataLocators:
    # 【查询条件区】
    # 用户编号
    QRY_USER_NO = (By.XPATH, "//*[@id=\"lineCpNo\"]")
    # 电表正反向
    QRY_METER_FR = (By.XPATH, "//*[@id=\"meterzfx\"]")
    QRY_METER_FR_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'正')]/../div[contains(text(),'%s')]")
    # 用户名称
    QRY_USER_NAME = (By.XPATH, "//*[@id=\"lineCpName\"]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
