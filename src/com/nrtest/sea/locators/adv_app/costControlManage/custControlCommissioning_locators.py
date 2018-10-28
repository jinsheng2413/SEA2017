# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: custControlCommissioning_locators.py
@time: 2018/8/23 0023 10:36
@desc:
'''
from selenium.webdriver.common.by import By


class CustControlCommissioning_locators:
    # 【查询条件】
    # 营销单号
    QRY_MARKETINF_SINGLE_NUM = (By.XPATH, "//div[@class=\"x-form-item \"]/label[contains(text(),'营销单号')]/../div/input")
    # 开始时间
    QRY_START_TIME = (By.XPATH, '//*[@name="startDate"]')
    # 下发状态
    QRY_PROVIDE_STATE = (By.XPATH, "//div[@class=\"x-form-item \"]/label[contains(text(),'下发状态')]/../div[1]/div/img")
    QRY_PROVIDE_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'下发失败')]/../div[%s]")

    # 结束时间
    QRY_END_TIME = (By.XPATH, '//*[@name="endDate"]')
    # 终端地址
    QRY_TERMIAL_ADDR = (By.XPATH, "//div[@class=\"x-form-item \"]/label[contains(text(),'终端地址')]/../div/input")
    # 用户编号
    QRY_USER_NUM = (By.XPATH, "//div[@class=\"x-form-item \"]/label[contains(text(),'用户编号')]/../div/input")
    # 用户名称
    QRY_USER_NAME = (By.XPATH, "//div[@class=\"x-form-item \"]/label[contains(text(),'用户名称')]/../div/input")
    # 按
    SELR_ARRANGE = (By.XPATH, "//label[contains(text(),'按')]/../div[1]/div/img")
    SELR_ARRANGE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'购电日期')]/../div[%s]")

    # 【操作区】
    BTN_QRY = (
        By.XPATH,
        "//div[@class=\" x-panel x-panel-noborder x-form-label-right x-column\"]//button[contains(text(),'查询')]")
    BTN_OUT = (By.XPATH, "//*[contains(text(),'退出')]")
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')
    TAB_ONE_ALL_CLASS = (By.XPATH, '(// div[@class =\"x-grid3-row-checker\"])[1]/../../../td[10]/div/a')

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByName("startDate")[0].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByName("endDate")[0].removeAttribute("readonly");'
