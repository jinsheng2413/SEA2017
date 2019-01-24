# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: unControlPlantGatherMon_locators.py
@time: 2018-11-06 15:45
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用→重点用户监测→非统调电厂管理→非统调电厂采集监测 tab1
class UnControlPlantGatherMon1_locators:
    # [显示区]
    # 节点名
    QRY_ORG = (By.XPATH, "//input[@id='unConGaOrgTextField']")
    # 开始时间
    QRY_START_DATE = (By.XPATH, "//input[@id='startDate']")
    # 结束时间
    QRY_END_DATE = (By.XPATH, "//input[@id='endDate']")
    # 发电方式
    QRY_GC_MODE = (By.XPATH, "//input[@id='monGenElecTypeCombox']")
    # 值（发电方式）
    QRY_GC_MODE_VALUE = (
    By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'火力')])[1]/../div[contains(text(),'%s')]")
    # 采集方式
    QRY_COLL_MODE = (By.XPATH, "//input[@id='monCommModelCombo']")
    # 值（采集方式）
    QRY_COLL_MODE_VALUE = (
    By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'CDMA')])[1]/../div[contains(text(),'%s')]")

    # 【操作区】
    # 【查询】
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")


# 第二个tab页
class UnControlPlantGatherMon2_locators:
    # [显示区]
    # 节点名
    QRY_ORG = (By.XPATH, "//input[@id='unConGaDetailOrgTextField']")
    # 发电方式
    QRY_GC_MODE = (By.XPATH, "//input[@id='monGenElecTypeDetCombox']")
    # 值（发电方式）
    QRY_GC_MODE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'%s')]")
    # 采集方式
    QRY_COLL_MODE = (By.XPATH, "//input[@id='monCommModelDetCombo']")
    # 值（采集方式）
    QRY_COLL_MODE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'%s')]")
    # 查询日期
    QRY_DATE = (By.XPATH, "//input[@id='startDetailDate']")
    # 户号
    QRY_CONS_NO = (By.XPATH, "//input[@id='consNoGather']")
    # 表资产编号
    QRY_METER_ASSET_NO = (By.XPATH, "//input[@id='meterNoGather']")
    # 终端资产号
    QRY_TMNL_ASSET_NO = (By.XPATH, "tmnlNoGather")

    # 【操作区】
    # 【查询】
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[3]")

    # 【js操作】
    # 开始时间，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[15].removeAttribute("readonly");'

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[2]")
