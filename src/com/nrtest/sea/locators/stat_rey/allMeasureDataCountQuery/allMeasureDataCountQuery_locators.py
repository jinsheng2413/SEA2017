# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: allMeasureDataCountQuery_locators.py
@time: 2018/11/2 10:41
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→全量数据统计查询→全量数据统计查询
class AllMeasureDataCountQueryLocators:
    # 用户类型
    # QRY_USER_TITLE = (
    #     By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'用户类型\')]/../../div[1]/div[1]//input")
    # QRY_WORK_USER_VALUE = (
    #     By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),\'专变用户\')]/../div[contains(text(),'%s')]")
    # 日期
    QRY_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),\'日期\')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')]")
    BTN_RE = (By.XPATH,
              "//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'重置')]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[6].removeAttribute("readonly");'
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
