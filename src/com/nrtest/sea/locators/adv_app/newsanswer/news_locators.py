# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: news_locators.py
@time: 2018-11-02 9:35
@desc:
"""

from selenium.webdriver.common.by import By


class News_Locators:
    # [显示区]
    # 供电单位
    QRY_ORG = (By.XPATH, "//label[contains(text(),'供电单位')]/../div/input")
    # 问题标题
    QRY_QUESTION_TITLE = (
        By.XPATH, "//label[contains(text(),'问题标题')]/../div/input")
    # 问题类型
    QRY_QUESTION_TYPE = (
        By.XPATH, "//label[contains(text(),'问题类型')]/../div/div/input")
    # 值（问题类型）
    QRY_QUESTION_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'BUG')]/../div[contains(text(),'%s')]")
    # 问题板块
    QRY_QUESTION_PLATE = (
        By.XPATH, "//label[contains(text(),'问题版块')]/../div/div/input")
    # 值（问题板块）
    QRY_QUESTION_PLATE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'数据采集')]/../div[contains(text(),'%s')]")
    # 紧急程度
    QRY_EMERGENCY_DEGREE = (
        By.XPATH, "//label[contains(text(),'紧急程度')]/../div/div/input")
    # 值（紧急程度）
    QRY_EMERGENCY_DEGREE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'紧急')]/../div[contains(text(),'%s')]")
    # 查询方式
    QRY_QUERY_METHOD = (
        By.XPATH, "//label[contains(text(),'查询方式')]/../div/div/input")
    # 值（查询方式）
    QRY_QUERY_METHOD_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'自己发布的')]/../div[contains(text(),'%s')]")
    # 问题状态
    QRY_QUESTION_STATUS = (
        By.XPATH, "//label[contains(text(),'问题状态')]/../div/div/input")
    # 值（问题状态）
    QRY_QUESTION_STATUS_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'已回复')]/../div[contains(text(),'%s')]")
    # 开始日期
    QRY_START_DATE = (
        By.XPATH, "//label[contains(text(),'开始日期')]/../div/div/input")
    # 结束日期
    QRY_END_DATE = (
        By.XPATH, "//label[contains(text(),'结束日期')]/../div/div/input")

    # 【操作区】
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[10].removeAttribute("readonly");'
    END_DATE_JS = 'document.getElementsByTagName("input")[11].removeAttribute("readonly");'
