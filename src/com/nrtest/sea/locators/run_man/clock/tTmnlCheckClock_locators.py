# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_locators.py
@time: 2018/10/30 11:11
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→时钟管理→终端对时
# 终端对时统计
class TmnlClockStaticLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[1]"))
    # 终端类型-下拉框
    TMNL_TYPE_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端类型')]/../div/div/img)[1]")
    # 终端类型
    TMNL_TYPE = (
        By.XPATH, '//div[@class=\"x-combo-list-inner\"]//div[contains(text(),"%s")]')
    #(By.XPATH, '(//div[@class =\"x-layer x-combo-list  x-resizable-pinned\"])[1]//*[contains(text(),"%s")]')
    # 终端厂商-下拉框
    TMNL_FAC_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端厂商')]/../div/div/img)[1]")
    # 终端厂商
    TMNL_FAC = (
        By.XPATH, '//div[@class=\"x-combo-list-inner\"]//div[contains(text(),"%s")]')
    # 日期
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[1]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("tmnlCheckClockMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[1]/div/div)[1]")


# 终端时钟明细


class TmnlClockDetailLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 偏差范围-下拉框
    OFFSET_RANGE_SEL = (
        By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'偏差范围')]/../div/div/img")
    # 偏差范围
    OFFSET_RANGE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'1分钟到5分钟')]/../div[contains(text(),'%s')]")
    # 终端类型-下拉框
    TMNL_TYPE_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端类型')]/../div/div/img)[2]")
    # 终端类型
    TMNL_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'低压集中器')]/../div[contains(text(),'%s')]")
    # 终端型号
    TMNL_MODEL = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'终端型号')]/../div/input")
    # 终端厂商-下拉框
    TMNL_FAC_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'终端厂商')]/../div/div/img)[2]")
    # 终端厂商
    TMNL_FAC = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'宁波三星')]/../div[contains(text(),'%s')]")
    # 终端地址
    TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'终端地址')]/../div/input")
    # 是否在线-下拉框
    IS_ONLINE_SEL = (
        By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'是否在线')]/../div/div/img")
    # 是否在线
    IS_ONLINE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'在线')]/../div[contains(text(),'%s')]")
    # 日期
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[2]/../div/div/input")
    # 对时结果-下拉框
    CALL_STATUS_SEL = (
        By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'对时结果')]/../div/div/img")
    # 对时结果
    CALL_STATUS = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'成功')]/../div[contains(text(),'%s')]")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("tmnlClockDetailMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")


# 自动对时策略配置


class AutoCheckPolicyLocators:
    # 【查询条件】
    # 节点
    NODE = (
        By.XPATH, ("//div[@class=\"x-form-item \"]//*[contains(text(),'节点')]/../div/input"))
    # 间隔周期-下拉框
    INTERVAL_CYCLE_SEL = (
        By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'间隔周期')]/../div/div/img")
    # 间隔周期
    INTERVAL_CYCLE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'4')])[1]/../div[text()='%s']")
    # 周期内自动对时次数-下拉框
    AUTO_TIMES_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'周期内自动对时次数')]/../div/div/img)[1]")
    # 周期内自动对时次数
    AUTO_TIMES = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'4')])[2]/../div[text()='%s']")
    # 自动对时开始日期
    QUERY_DATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'自动对时开始日期')]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")


# 终端手工对时


class TmnlManualCheckLocators:
    # 【查询条件】
    # 节点
    NODE = '后续通过选择终端'
