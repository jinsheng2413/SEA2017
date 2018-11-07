# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: workQuery2017_locators.py
@time: 2018/11/1 14:17
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→工单查询→工单查询2017
class WorkCount2017Locators:
    # 工单类型
    QRY_WORK_TITLE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),\'工单类型\')]/../../div[1]/div[1]//input)[1]")
    QRY_WORK_TITLE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'采集运维工单\')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")


class WorkQuery2017Locators:
    # 【查询条件区】
    # 工单编号
    QRY_WORK_NO = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'工单编号\')]/../../div[1]/div[1]//input")
    # 工单处理人
    QRY_WORK_MAN = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'工单处理人\')]/../../div[1]/div[1]//input")
    # 工单类型
    QRY_WORK_TITLE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),\'工单类型\')]/../../div[1]/div[1]//input)[2]")
    QRY_WORK_TITLE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'采集运维工单\')]/../div[contains(text(),'%s')]")
    # 工单状态
    QRY_WORK_STATUS = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'工单状态\')]/../../div[1]/div[1]//input")
    QRY_WORK_STATUS_VALUE = (
        By.XPATH,
        "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'待处理工单\')]/../div[contains(text(),'%s')]")
    # 工单发生时间
    QRY_STARTDATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'工单发生时间\')]/../../div[1]/div[1]//input")
    # 工单完成时间
    QRY_ENDDATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'工单完成时间\')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById(\'workQuery2017_StartDate\').removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById(\'workQuery2017_EndDate\').removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
