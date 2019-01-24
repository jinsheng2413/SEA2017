# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyStat_locators.py
@time: 2018/10/29 0029 10:40
@desc:
"""
from selenium.webdriver.common.by import By


# 高级应用→重点用户检测→分布式电源管理→分布式电源接入统计


class DistributedEnergyStatLocators:
    # 【查询条件区】
    # 日期
    QRY_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'日期')]/../../div[1]/div[1]//input")
    # 发电量消纳方式
    QRY_ABSO_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'发电量消纳方式')]/../../div[1]/div[1]//input")
    QRY_ABSO_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'全部自用')]/../div[contains(text(),'%s')]")
    # 发电类型
    QRY_POWER_MODE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'发电类型')]/../../div[1]/div[1]//input")
    QRY_POWER_MODE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'水力')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName(\'input\')[5].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
