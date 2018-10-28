# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: waveArchives_Locators.py
@time: 2018/9/25 0025 13:22
@desc:
'''
from selenium.webdriver.common.by import By


# 基本应用--》档案管理--》载波档案矫正
class WaveArchives_Locators:
    # 【查询条件区】
    # 台区编号
    QRY_ZONE_NO = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'台区编号')])[1]/../../div[1]/div[1]/input")
    # 统计时间
    QRY_COUNT_TIME = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'统计时间')])[1]/../../div[1]/div[1]/div/input")
    # 台区名称
    QRY_ZONE_NAME = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'台区名称')])[1]/../../div[1]/div[1]/input")
    # 统计分类
    QRY_COUNT_TYPE = (By.XPATH, "//*[@name=\"archivesTypeCombox\"]")
    QRY_COUNT_TYPE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("startDate").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
