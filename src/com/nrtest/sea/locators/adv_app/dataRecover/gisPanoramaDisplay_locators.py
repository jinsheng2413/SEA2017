# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: gisPanoramaDisplay_locators.py
@time: 2018/10/18 0018 10:40
@desc:
"""
from selenium.webdriver.common.by import By


# 统计查询→数据分析→电量分析→电量数据查询
class GisPanoramaDisplayLocators:
    # 【查询条件区】
    # 用户类型
    QRY_USER_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户类型')]/../../div[1]/div[1]//input")
    QRY_USER_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变用户')]/../div[contains(text(),'%s')]")

    # 逐日显示
    QRY_DAY_DISPLAY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'逐日显示')]/../../div[1]/div[1]//input")
    QRY_DAY_DISPLAY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'是')]/../div[contains(text(),'%s')]")

    # 查询时间
    QRY_QUERY_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'查询时间')]/../../div[1]/div[1]//input")
    #
    QRY_ = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[11].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
