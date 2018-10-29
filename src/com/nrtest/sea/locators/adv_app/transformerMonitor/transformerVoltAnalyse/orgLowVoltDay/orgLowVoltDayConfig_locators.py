# -*- coding:utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/24 20:42
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用--》配变监测分析--》电压质量分析--》低压用户电压分析
# 低压用户电压监测配置
class OrgLowVoltDayConfigLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[1]")
    # 是否电压监测-下拉框
    IS_VOLT_MONITOR_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'是否电压监测')]/../div/div/img)[1]")
    # 是否电压监测
    IS_VOLT_MONITOR = (By.XPATH, '//div[@class=\"x-combo-list-inner\"]//div[contains(text(),"%s")]')

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[3]")

    # 【显示区】
    TABLE_DATA = (By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[3]/div/div)[1]")
