# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_locators.py
@time: 2018/11/12 9:20
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→采集运维平台→采集终端质量评价
# 终端质量评价统计
class TmnlQualityEvalStaticLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[1]"))
    # 用户类型-下拉框
    CONS_TYPE_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'用户类型')]/../div/div/img)[1]")
    # 用户类型
    CONS_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')]")
    # 月份
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'月份')])[1]/../div/div/input")
    # 终端厂家-下拉框
    TMNL_FACTORY_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端厂家')]/../div/div/img)[1]")
    # 终端厂家
    TMNL_FACTORY = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'上海协同')]/../div[contains(text(),'%s')]")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[1]/div/div)[1]")


# 终端质量评价明细
class TmnlQualityEvalDetailLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 用户类型-下拉框
    CONS_TYPE_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'用户类型')]/../div/div/img)[2]")
    # 用户类型
    CONS_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')]")
    # 故障严重程度-下拉框
    FAULT_SEVERITY_SEL = (By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'故障严重程度')]/../div/div/img")
    # 故障严重程度
    FAULT_SEVERITY = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'严重')]/../div[contains(text(),'%s')]")
    # 终端厂家-下拉框
    TMNL_FACTORY_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端厂家')]/../div/div/img)[1]")
    # 终端厂家
    TMNL_FACTORY = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'上海协同')]/../div[contains(text(),'%s')]")
    # 故障类别-下拉框
    FAULT_TYPE_SEL = (By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'故障类别')]/../div/div/img")
    # 故障类别
    FAULT_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'确认故障')]/../div[contains(text(),'%s')]")
    # 故障开始日期
    START_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'故障开始日期')]/../div/div/input")
    # 故障结束日期
    END_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'故障结束日期')]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询开始日期，删除readonly属性
    QUERY_START_DATE_JS = 'document.getElementById("startDateForTmnlQualEvalD").removeAttribute("readonly");'
    # 查询结束日期，删除readonly属性
    QUERY_END_DATE_JS = 'document.getElementById("endDateForTmnlQualEvalD").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")
