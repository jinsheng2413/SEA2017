# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: collectSuccessRateStat_locators.py
@time: 2018/9/30 0030 13:55
@desc:
'''
from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→采集质量分析→采集成功率综合统计
class CollectSuccessRateStatLocators:
    # 【查询条件区】
    # 查询日期
    QRY_CHECK_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'查询日期')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 查询时间，删除readonly属性
    CHECK_DATE_JS = "document.getElementsByTagName('input')[8].removeAttribute(\"readonly\");"

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
