# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkResultStat_locators.py
@time: 2018/11/19 0019 10:34
@desc:
"""
from selenium.webdriver.common.by import By


# 系统管理--》档案核查管理--》核查结果统计查询
class CheckResultStatLocators:
    # 【查询条件区】
    # 开始时间
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始日期')]/../../div[1]/div[1]//input")
    # 结束时间
    QRY_END_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'结束日期')]/../../div[1]/div[1]//input")
    # 任务类型
    QRY_TASK_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'任务类型')]/../../div[1]/div[1]//input")
    QRY_TASK_TYPE_VALUE = (
        By.XPATH,
        "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'电网结构核查')]/../..//div[contains(text(),'%s')]")
    # 异常类型
    QRY_EXCEPTION_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'异常类型')]/../../div[1]/div[1]//input")
    # 台区编号
    QRY_ZONE_AREA_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'台区编号')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[7].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName(\'input\')[8].removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
