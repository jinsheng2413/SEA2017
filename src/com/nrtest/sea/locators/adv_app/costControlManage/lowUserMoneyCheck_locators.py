# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserMoneyCheck_Page.py
@time: 2018/8/9 0009 13:57
@desc:
"""
from selenium.webdriver.common.by import By


class BalanceCountLocator:
    # 【查询条件】
    # 数据日期
    QRY_DATA_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'数据日期')]/../div/div/input")

    # 【操作区】
    # 查询按钮
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//*[@class=\"x-grid3-row-checker\"])[1]')
    # 供电单位明细
    TAB_ONE_ELE_COMPANY = (
        By.XPATH, '(//*[@class=\"x-grid3-row-checker\"])[1]/../../../td[2]/div/a')
    # 10院内用户总数
    TAB_ONE_TEN_USER_ALL = (
        By.XPATH, '(//*[@class=\"x-grid3-row-checker\"])[1]/../../../td[5]/div/a')
    # 50院内用户总数
    TAB_ONE_FIFTY_USER_ALL = (
        By.XPATH, '(//*[@class=\"x-grid3-row-checker\"])[1]/../../../td[7]/div/a')
    # 超50元用户总数
    TAB_ONE_MORE_FIFTY_USER_ALL = (
        By.XPATH, '(//*[@class=\"x-grid3-row-checker\"])[1]/../../../td[9]/div/a')

    # 余额查看
    BAL_CHECK = (
        By.XPATH, "(//*[contains(text(),'余额查看')])[@class=\"x-tab-strip-text \"]")
    # 余额统计
    BAL_COUNT = (
        By.XPATH, "(//*[contains(text(),'余额统计')])[@class=\"x-tab-strip-text \"]")


class BalanceCheckLocator:
    # 【查询条件】
    # 工单编号
    QRY_WORK_ORDER = (By.XPATH, '//*[@id="appNoFieldb"]')
    # 用户编号
    QRY_USER_ORDER = (By.XPATH, '//*[@id="staffNoFieldb"]')
    # 终端地址
    QRY_TERMINAL_ADDR = (By.XPATH, '//*[@id="tmnlAddrFieldb"]')
    # 电表地址
    QRY_METER_ADDR = (By.XPATH, '//*[@id="meterAddrFieldb"]')
    # 抄表段号
    QRY_METER_READING_NUMBER = (By.XPATH, '//*[@id="readMeterSegNoFieldb"]')
    # 用户名称
    QRY_USER_NAME = (By.XPATH, '//*[@id="readMeterConsName"]')
    # 电表局编号
    QRY_ELE_METER_BUREEA_ORDER = (By.XPATH, '//*[@id="readMeterAssetNo"]')
    # 接收时间
    QRY_RECEIVE_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'接收时间：')]/../div/div/input")
    # 末
    QRY_END_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'（末）')]/../div/div/input")
    # 执行状态
    QRY_EXECUTE_STATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'执行状态:')]/../div/div/input")
    # 执行状态选择的值
    QRY_EXECUTE_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'执行成功')]/../div[%s]")
    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")
    # 余额查看
    BAL_CHECK = (
        By.XPATH, "(//*[contains(text(),'余额查看')])[@class=\"x-tab-strip-text \"]")
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//*[@class=\"x-grid3-row-checker\"])[1]')
