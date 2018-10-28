# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: powerSortAnalyse_locators.py
@time: 2018/10/18 0018 9:27
@desc:
'''
from selenium.webdriver.common.by import By


# 统计查询--》数据分析--》电量分析--》电量排名分析
class PowerSortAnalyseLocators:
    # 【查询条件区】
    # 排名数量
    QRY_RANKING_NUMBER = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'排名数量')]/../../div[1]/div[1]//input")
    # 用户类型
    QRY_USER_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户类型')]/../../div[1]/div[1]//input")
    QRY__USER_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')]")
    # 开始时间
    QRY_START_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始日期')]/../../div[1]/div[1]//input")
    # 结束时间
    QRY_END_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'结束日期')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[5].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName(\'input\')[6].removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
