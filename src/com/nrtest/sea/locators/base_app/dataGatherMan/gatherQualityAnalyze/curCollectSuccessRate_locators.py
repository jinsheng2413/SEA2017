# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: curCollectSuccessRate_locators.py
@time: 2018/10/11 0011 10:09
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→采集质量分析→实时采集成功率
class CurCollectSuccessRateLocators:
    # 【查询条件区】
    # 开始时间
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始时间')]/../../div[1]/div[1]//input")
    # 结束时间
    QRY_END_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'结束时间')]/../../div[1]/div[1]//input")

    # 统计页面日期时间
    QRY_DATE_TIME_COUNT = (By.XPATH, "//*[@id=\"curReadDate\"]")
    # 台区名称
    QRY_PLATFORM_NAME = (By.XPATH, "//*[@id=\"failDetailTqmc\"]")
    # 台区编号
    QRY_PLATFORM_NO = (By.XPATH, "//*[@id=\"failDetailTqno\"]")
    # 明细页面日期时间
    QRY_DATE_TIME_DETAIL = (By.XPATH, "//*[@id=\"curFailDetail_statDate\"]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    BTN_QRY_COUNT = (By.XPATH,
                     "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")
    BTN_QRY_DETAIL = (By.XPATH,
                      "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[3]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = "document.getElementsByTagName('input')[7].removeAttribute(\"readonly\");"
    # 结束时间，删除readonly属性
    END_DATE_JS = "document.getElementsByTagName('input')[8].removeAttribute(\"readonly\");"
    JS_COUNT = "document.getElementById('curReadDate').removeAttribute(\"readOnly\")"
    JS_DETAIL = "document.getElementById('curFailDetail_statDate').removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
