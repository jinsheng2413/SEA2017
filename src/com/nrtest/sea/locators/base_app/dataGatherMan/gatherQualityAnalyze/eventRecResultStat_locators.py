# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: eventRecResultStat_locators.py
@time: 2018/9/28 0028 11:33
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→采集质量分析→事件记录结果统计
class EventRecResultStatLocators:
    # 【查询条件区】
    # 起始日期
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'起始日期')]/../../div[1]/div[1]//input")
    #
    QRY_END_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终止日期')]/../../div[1]/div[1]//input")

    # 事件类型
    QRY_EVENT_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'事件类型')]/../../div[1]/div[1]//img")
    QRY_EVENT_TYPE_VALUE = (By.XPATH,
                            "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'ERC1数据初始化和版本变更')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = "document.getElementsByTagName('input')[6].removeAttribute(\"readonly\");"
    # 结束时间，删除readonly属性
    END_DATE_JS = "document.getElementsByTagName('input')[7].removeAttribute(\"readonly\");"
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
