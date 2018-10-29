# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: elePricePara_locators.py
@time: 2018/8/15 0015 14:01
@desc:
"""
from selenium.webdriver.common.by import By


class ElePricePara_locators:
    # 【查询条件】
    # 工单编号
    QRY_EMPLOYEE_NUM = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'工单编号')]/../../div[1]/div[1]/input")
    # 用户编号
    QRY_USER_NUM = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户编号')]/../../div[1]/div[1]/input")
    # 终端地址
    QRY_TERMINAL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[2]/div[1]/input")
    # 电表地址
    QRY_METER_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'电表地址')]/../../div[2]/div[1]/input")
    # 抄表段号
    QRY_METER_READING_NUMBER = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'抄表段号')]/../../div[2]/div[1]/input")
    # 接收时间
    QRY_RECEIVE_DATE = (By.XPATH, '//*[@id="appRecieveStartTime"]')
    # 结束时间
    QRY_END_TIME = (By.XPATH, '//*[@id="appRecieveEndTime"]')
    # 执行状态
    QRY_EXECUTE_STATE = (By.XPATH, '//*[@id="elecPriceParamStatus"]')
    # 执行状态的值
    QRY_EXECUTE_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'执行失败')]/../div[%s]")
    # 任务类型
    QRY_TASK_CATA = (By.XPATH, '// *[ @ id = "elecPriceParamType"]')
    QRY_TASK_CATA_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'时区参数')]/../div[%s]")
    # 【操作区】
    BTN_QRY = (
        By.XPATH,
        "//div[@class=\" x-panel x-panel-noborder x-form-label-right x-column\"]//button[contains(text(),'查询')]")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("appRecieveStartTime").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("appRecieveEndTime").removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')
