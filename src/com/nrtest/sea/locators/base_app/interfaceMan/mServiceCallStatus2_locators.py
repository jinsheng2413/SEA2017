# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mServiceCallStatus2_locators.py
@time: 2018-10-31 8:55
@desc:
'''

from selenium.webdriver.common.by import By


# 基本应用--》接口管理--》营销业务接口--》服务调用情况
class MServiceCallStatus2Locators:
    # [显示区]
    # 业务系统
    QRY_BUSINESS_SYSTEM = (By.XPATH, "//label[contains(text(),'业务系统')]/../div/div/input")
    # 执行状态的值
    QRY_BUSINESS_SYSTEM_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'营销业务应用')]/../div[contains(text(),'%s')]")
    # 服务名称
    QRY_BUSINESS_NAME = (By.XPATH, "//label[contains(text(),'服务名称')]/../div/div/input")
    # 执行状态的值
    QRY_BUSINESS_NAME_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'数据接入')]/../div[contains(text(),'%s')]")
    # 调用时间（开始）
    QRY_DATE_BEGIN = (By.XPATH, "//label[contains(text(),'调用时间')]/../div/div/input")
    # 结束时间
    QRY_DATE_END = (By.XPATH, "//label[contains(text(),'至')]/../div/div/input")

    # [操作区]
    # 查询
    BTN_QUERY = (By.XPATH, "//button[text()='统计']")

    # [显示区]
    TAB_ONE = (By.XPATH, "//div[@class='x-grid3-scroller']")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'
