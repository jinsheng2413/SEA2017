# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/24 20:42
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用--》配变监测分析--》电压质量分析--》低压用户电压分析
# 台区低电压日统计
class OrgLowVoltDayStaticLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'节点名')]/../div/input)[1]")
    # 开始日期
    START_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'开始日期')]/../div/div/input)[1]")
    # 结束日期
    END_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'结束日期')]/../div/div/input)[1]")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【js操作】
    # 开始日期，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[4].removeAttribute("readonly");'
    # 结束日期，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[1]/div/div)[1]")
