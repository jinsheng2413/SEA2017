# -*- coding:utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/24 20:42
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用--》配变监测分析--》电压质量分析--》B/C类电压监测点
# B/C类电压监测点查询
class BcVoltMonitorPointQueryLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[1]"))
    # 监测点类型-下拉框
    MONITOR_POINT_TYPE_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'监测点类型')]/../div/div/img)[1]")
    # 监测点类型
    MONITOR_POINT_TYPE = (By.XPATH, '//div[@class=\"x-combo-list-inner\"]//div[contains(text(),"%s")]')
    # 监测点名称
    MONITOR_POINT_NAME = (By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'监测点名称')]/../div/input)[1]"))

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TABLE_DATA = (By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[1]/div/div)[1]")
