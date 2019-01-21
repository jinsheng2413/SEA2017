# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: faultHandler_locators.py
@time: 2018/11/12 0012 9:31
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→采集运维平台→采集故障处理→专变故障处理
class FaultHandlerLocators:
    #【查询条件区】
    # 故障来源
    QRY_FAULT_FROM = (By.XPATH, "//*[@id=\"dataSrc\"]")
    QRY_FAULT_FROM_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'计量异常')]/../div[contains(text(),'%s')]")
    # 故障严重程度
    QRY_FAULT_SEVERITY = (By.XPATH, "//*[@id=\"severeLevel\"]")
    QRY_FAULT_SEVERITY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'I 级')]/../div[contains(text(),'%s')]")
    #故障开始日期
    QRY_FAULT_START_DATE = (By.XPATH, "//*[@id=\"handlerStartDate\"]")
    #流程状态
    QRY_PROCESS_STAUS = (By.XPATH, "//*[@id=\"flowStatus\"]")
    QRY_PROCESS_STAUS_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新异常')]/../div[contains(text(),'%s')]")
    #故障结束日期
    QRY_FAULT_END_DATE = (By.XPATH, "//*[@id=\"handlerEndDate\"]")
    #
    QRY_ = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")

    # 故障类型
    QRY_FAULT_TYPE = (By.NAME, 'isValid')

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("handlerStartDate").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("handlerEndDate").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")


class FaultFeedBackLocators:
    # 【查询条件区】
    # 故障来源
    QRY_FAULT_FROM = (By.XPATH, "//*[@id=\"feedbackDataSrc\"]")
    QRY_FAULT_FROM_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'计量异常')]/../div[contains(text(),'%s')]")
    # 故障严重程度
    QRY_FAULT_SEVERITY = (By.XPATH, "//*[@id=\"feedbacksevereLevel\"]")
    QRY_FAULT_SEVERITY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'I 级')]/../div[contains(text(),'%s')]")
    # 故障开始日期
    QRY_FAULT_START_DATE = (By.XPATH, "//*[@id=\"feedbackStartDate\"]")
    # 流程状态
    QRY_PROCESS_STAUS = (By.XPATH, "//*[@id=\"feedbackflowStatus\"]")
    QRY_PROCESS_STAUS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新异常')]/../div[contains(text(),'%s')]")
    # 故障结束日期
    QRY_FAULT_END_DATE = (By.XPATH, "//*[@id=\"feedbackEndDate\"]")
    #
    QRY_ = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")

    # 故障类型
    QRY_FAULT_TYPE = (By.NAME, 'isValid')

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("feedbackStartDate").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("feedbackflowStatus").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")


     
     
     