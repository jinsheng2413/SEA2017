# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_locators.py
@time: 2018/11/1 16:11
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→时钟管理→时钟运行质量分析
# 按单位统计
class StaticByOrgLocators:
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
    # 电能表厂商-下拉框
    MET_FAC_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'电能表厂商')]/../div/div/img)[1]")
    # 电能表厂商
    MET_FAC = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),' ABB公司')]/../div[contains(text(),'%s')]")
    # 日期
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[1]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("unitMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[1]/div/div)[1]")


# 按厂家统计
class StaticByFacLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 月份
    QUERY_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'月份')]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("compStartMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")


# 频繁对时终端
class FrequentlyCheckTmnlLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 终端类型-下拉框
    TMNL_TYPE_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端类型')]/../div/div/img)[1]")
    # 终端类型
    TMNL_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'低压集中器')]/../div[contains(text(),'%s')]")
    # 终端型号
    TMNL_MODEL = (
        By.XPATH, ("//div[@class=\"x-form-item \"]//*[contains(text(),'终端型号')]/../div/input"))
    # 终端厂商-下拉框
    TMNL_FAC_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端厂商')]/../div/div/img)[2]")
    # 终端厂商
    TMNL_FAC = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'宁波三星')]/../div[contains(text(),'%s')]")
    # 终端资产号
    TMNL_ASSET_NO = (
        By.XPATH, ("//div[@class=\"x-form-item \"]//*[contains(text(),'终端资产号')]/../div/input"))
    # 日期
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[2]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("freqTmnlMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")


# 频繁对时电表
class FrequentlyCheckMetLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 电能表厂商-下拉框
    MET_FAC_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'电能表厂商')]/../div/div/img)[2]")
    # 电能表厂商
    MET_FAC = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'ABB公司')]/../div[contains(text(),'%s')]")
    # 电表类别-下拉框
    MET_TYPE_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'电表类别')]/../div/div/img)[1]")
    # 电表类别
    MET_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'有功表')]/../div[contains(text(),'%s')]")
    # 电能表资产号
    MET_ASSET_NO = (
        By.XPATH, ("//div[@class=\"x-form-item \"]//*[contains(text(),'电能表资产号')]/../div/input"))
    # 用户编号
    CONS_NO = (
        By.XPATH, ("//div[@class=\"x-form-item \"]//*[contains(text(),'用户编号')]/../div/input"))
    # 日期
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[2]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("freqMeterMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")
