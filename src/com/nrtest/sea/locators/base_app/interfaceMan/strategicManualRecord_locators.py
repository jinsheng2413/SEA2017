# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: strategicManualRecord_locators.py
@time: 2018-11-08 9:45
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→接口管理→人工补录
class StrategicManualRecord_Locators:
    # [左边树区]
    # 电网结构
    QRY_DWJG = (By.XPATH, "//span[contains(text(),'电网结构')]")
    # 供电单位
    QRY_ORG = (By.XPATH, "(//span[contains(text(),'国网冀北电力有限公司')])[2]")
    # 【查询条件区】
    # 采集点名
    QRY_GATHERPOINT_NAME = (By.XPATH, "//label[contains(text(),'采集点名')]/../div/input")
    # 电表名称
    QRY_METER_NAME = (By.XPATH, "//label[contains(text(),'电表名称')]/../div/input")
    # 处理类型
    QRY_METER_ADDR = (By.XPATH, "//label[contains(text(),'电表地址')]/../div/input")
    # 日期
    QRY_DATE = (By.XPATH, "(//label[contains(text(),'日期')]/../div/div/input)[1]")

    # 【操作区】
    BTN_QRY = (By.XPATH, "//*[text()='查询']")

    # 【js区】
    # 开始时间，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
