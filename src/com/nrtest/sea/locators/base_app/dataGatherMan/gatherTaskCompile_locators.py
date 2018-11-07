# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: gatherTaskCompile_locators.py
@time: 2018/9/28 0028 14:53
@desc:
"""
from selenium.webdriver.common.by import By


class GatherTaskCompileLocators:
    # 【查询条件区】
    # 任务类型
    QRY_TASK_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'任务类型')]/../../div[1]/div[1]//input")
    QRY_TASK_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'负荷类')]/../div[contains(text(),'%s')]")

    # 终端类型
    QRY_TMAL_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端类型')]/../../div[1]/div[1]//input")
    QRY_TMAL_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'负荷控制终端')]/../div[%s]")

    # 任务编号
    QRY_TAST_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'任务编号')]/../../div[1]/div[1]//input")

    # 任务名称
    QRY_TASK_NAME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'任务名称')]/../../div[1]/div[1]//input")

    # 任务状态
    QRY_TASK_STATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'任务状态')]/../../div[1]/div[1]//input")

    QRY_TASK_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'启动')]/../div[contains(text(),'%s')]")

    # 终端地址
    QRY_TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]//input")

    # 采集点名称
    QRY_COLLECTION_POINT_NAME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'采集点名称')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[2]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
