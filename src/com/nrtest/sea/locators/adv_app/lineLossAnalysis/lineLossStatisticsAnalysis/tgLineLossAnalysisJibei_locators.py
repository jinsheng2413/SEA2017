# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossAnalysisJibei_locators.py
@time: 2018/10/31 16:17
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→线损分析→线损统计分析→台区线损分析（冀北）
class TgLineLossAnalysisJibeiLocators:
    # %前，输入框
    QRY_INPUT = (By.XPATH, '//label[text()="%"]/../../../../preceding-sibling::td[1]//input')
    # %后，下拉选择按钮
    QRY_SEL = (By.XPATH, '//label[text()="%"]/../../../../following-sibling::td[1]//img')

    # # 台区编号
    # QRY_TG_NO = (By.XPATH, '//label[contains(text(),"台区编号")]/../div/input')
    # # 台区名称
    # QRY_TG_NAME = (By.XPATH, '//label[contains(text(),"台区名称")]/../div/input')
    # # 安装率
    # QRY_INSTALL_RATE = (
    #     By.XPATH, '//label[contains(text(),"安")]/../div/div/input')
    # QRY_INSTALL_RATE_VALUE = (
    #     By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # QRY_INSTALL_RATE_INPUT = (
    #     By.XPATH, '//input[@class=" x-form-text x-form-field x-form-num-field "]')
    # # 抄读成功率
    # QRY_READ_SUCCESS_RATE = (
    #     By.XPATH, '//label[contains(text(),"抄读成功率:")]/../div/div/input')
    # QRY_READ_SUCCESS_RATE_VALUE = (
    #     By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # QRY_READ_SUCCESS_RATE_INPUT = (
    #     By.XPATH, '(//input[@class=" x-form-text x-form-field x-form-num-field "]）[3]')
    # # 线损率
    # QRY_LINE_LOSS_RATE = (
    #     By.XPATH, '//label[contains(text(),"线")]/../div/div/input')
    # QRY_LINE_LOSS_RATE_VALUE = (
    #     By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # QRY_LINE_LOSS_RATE_INPUT = (
    #     By.XPATH, '(//input[@class=" x-form-text x-form-field x-form-num-field "]）[5]')
    # # 查询日期
    # QRY_DATE = (By.XPATH, '//label[contains(text(),"查询日期")]/../div/div/input')
    # # 查询按钮
    # BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
    #
    # # 【JS属性】
    # # 查询日期，删除readonly属性
    # DATE_JS = 'document.getElementsByTagName("input")[24].removeAttribute("readonly");'
