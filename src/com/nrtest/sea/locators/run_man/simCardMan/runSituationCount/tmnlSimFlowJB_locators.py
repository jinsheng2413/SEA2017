# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: tmnlSimFlowJB_locators.py
@time: 2018-11-12 9:22
@desc:
"""

from selenium.webdriver.common.by import By


# 运行管理--》SIM卡管理--》运行情况分析--》终端流量统计（冀北）
# 第一个tab页
class TmnlSimFlowJB_1Locators:
    # [显示区]
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//input[@id='tmnlAddr']")
    # SIM卡号
    QRY_SIM_NO = (By.XPATH, "//input[@id='tmnlSimNo']")
    # 日期
    QRY_START_DATE = (By.XPATH, "(//label[contains(text(),'日期')]/../div/div/input)[1]")
    # 至 日期
    QRY_END_DATE = (By.XPATH, "(//label[contains(text(),'日期')]/../div/div/input)[2]")

    # 【操作区】
    # 查询
    BTN_QUERY = (By.XPATH, "//button[contains(text(),'查询')]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'


# 第二个tab页
class TmnlSimFlowJB_2Locators:
    # [显示区]
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//input[@id='tmnlAddrY']")
    # SIM卡号
    QRY_SIM_NO = (By.XPATH, "//input[@id='tmnlSimNoY']")
    # 日期
    QRY_DATE = (By.XPATH, "(//label[contains(text(),'日期')]/../div/div/input)[3]")
    # 全部
    QRY_ALL = (By.XPATH, "//label[contains(text(),'全部')]")
    # 正常
    QRY_NORMAL = (By.XPATH, "//label[contains(text(),'正常')]")
    # 零流量
    QRY_ZERO_FLOW = (By.XPATH, "//label[contains(text(),'零流量')]")
    # 超流量
    QRY_OVER_FLOW = (By.XPATH, "//label[contains(text(),'超流量')]")

    # 【操作区】
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[2]")

    # 【js操作】
    # 开始时间，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[13].removeAttribute("readonly");'
