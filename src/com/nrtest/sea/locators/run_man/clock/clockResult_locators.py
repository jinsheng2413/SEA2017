# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_locators.py
@time: 2018/11/1 14:11
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→时钟管理→对时结果分析
# 对时结果分析
class ClockResultStaticLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[1]"))
    # 终端厂商-下拉框
    TMNL_FAC_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端厂商')]/../div/div/img)[1]")
    # 终端厂商
    TMNL_FAC = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'宁波三星')]/../div[contains(text(),'%s')]")
    # 开始时间
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'开始时间')])[1]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("testMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[1]/div/div)[1]")


# 对时结果明细
class ClockResultDetailLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 类 别-下拉框
    CLOCK_MODEL_SEL = (
        By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'类            别:')]/../div/div/img")
    # 类 别
    CLOCK_MODEL = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'手工对时')]/../div[contains(text(),'%s')]")
    # 电表资产号
    MET_ASSET_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'电表资产号')]/../div/input")
    # 终端资产号
    TMNL_ASSET_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'终端资产号')]/../div/input")
    # 终端地址
    TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'终端地址')]/../div/input")
    # 月份
    QUERY_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'月            份:')]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("DetailStartMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")
