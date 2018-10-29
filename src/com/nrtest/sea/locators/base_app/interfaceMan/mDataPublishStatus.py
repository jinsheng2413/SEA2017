# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mDataPublishStatus.py
@time: 2018-09-21 9:07
@desc:
"""

from selenium.webdriver.common.by import By


class MDataPublishStatus_locators:
    # [显示区]
    # 供电单位
    QRY_ORG = (By.XPATH, "//label[contains(text(),'供电单位')]/../div/input")
    # 业务系统
    QRY_BUSINESS_SYSTEM = (By.XPATH, "//label[contains(text(),'业务系统')]/../div/div/input")
    QRY_BUSINESS_SYSTEM_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'%s')]")
    # 开始时间
    QRY_DATE_BEGIN = (By.XPATH, "//label[contains(text(),'发布时间')]/../div/div/input")
    # 结束时间
    QRY_DATE_END = (By.XPATH, "//label[contains(text(),'至')]/../div/div/input")

    # [操作区]
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[@class=\" x-btn-text\"])[4]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//table[@class=\"x-grid3-row-table\"])[1]")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("mDataPublishDateFrom").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("mDataPublishDateTo").removeAttribute("readonly");'
