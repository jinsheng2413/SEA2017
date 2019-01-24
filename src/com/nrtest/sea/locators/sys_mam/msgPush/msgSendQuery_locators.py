# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: msgSendQuery_locators.py
@time: 2018/11/22 13:42
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理→信息定制→推送信息定制→手机订阅→短信发送查询
class MsgSendQueryLocators:
    # 用户编号
    QRY_CONS_NO = (By.XPATH, '//label[contains(text(),"用户编号")]/../div/input')
    # 开始时间
    QRY_START_DATE = (By.XPATH, '//label[contains(text(),"开始时间")]/../div/div/input')
    # 结束时间
    QRY_END_DATE = (By.XPATH, '//label[contains(text(),"至")]/../div/div/input')
    # 发送状态
    QRY_SEND_STATUS = (By.XPATH, '//label[contains(text(),"发送状态")]/../div/div/img')
    QRY_SEND_STATUS_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 发送方式
    QRY_SEND_MODE = (By.XPATH, '//label[contains(text(),"发送方式")]/../div/div/img')
    QRY_SEND_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 发送人
    QRY_SEND_MAN = (By.XPATH, '//label[contains(text(),"发送人")]/../div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【JS属性】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
