# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: batchFetch_locators.py
@time: 2018/10/26 0026 14:07
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用--》数据采集管理--》数据召测--》批量巡测
class BatchFetchLocators:
    # 【查询条件区】
    # 任务名称
    QRY_TASK_NAME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'任务名称')]/../../div[1]/div[1]//input")
    # 操作人
    QRY_PERFORMER = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'操作人')]/../../div[1]/div[1]//input")

    # 有效性
    QRY_EFFECTIVENESS = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'有效性')]/../../div[1]/div[1]//input")
    QRY_EFFECTIVENESS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'无效')]/../div[contains(text(),'%s')]")
    # 开始时间
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始时间')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH, "//button[contains(text(),'查询')]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[6].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
