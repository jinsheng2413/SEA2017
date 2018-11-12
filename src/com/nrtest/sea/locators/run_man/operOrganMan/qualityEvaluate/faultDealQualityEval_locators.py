# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_locators.py
@time: 2018/11/12 9:20
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→采集运维平台→故障处理质量评价
# 故障处理质量统计
class FaultDealQualityStaticLocators:
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


# 故障处理质量明细
class FaultDealQualityDetailLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 用户类型-下拉框
    CONS_TYPE_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'用户类型')]/../div/div/img)[2]")
    # 用户类型
    CONS_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')]")
    # 月份
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'月份')])[2]/../div/div/input")
    # 流程状态-下拉框
    FLOW_STATUS_SEL = (
        By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'流程状态')]/../div/div/img")
    # 流程状态
    FLOW_STATUS = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'挂起')]/../div[contains(text(),'%s')]")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("statDateForQualDetail").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")


# 人员处理明细
class StaffDealDetailLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 用户类型-下拉框
    CONS_TYPE_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'用户类型')]/../div/div/img)[2]")
    # 用户类型
    CONS_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')]")
    # 月份
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'月份')])[2]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("statDateFormemDetail").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")

