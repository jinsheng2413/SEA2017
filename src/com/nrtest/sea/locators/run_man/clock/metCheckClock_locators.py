# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_locators.py
@time: 2018/11/1 9:11
@desc:
"""
from selenium.webdriver.common.by import By


# 运行管理→时钟管理→电能表对时
# 电表时钟月统计
class MetClockMonthStaticLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[1]"))
    # 电表类别-下拉框
    MET_TYPE_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'电表类别')]/../div/div/img)[1]")
    # 电表类别
    MET_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'有功表')]/../div[contains(text(),'%s')]")
    # 电能表厂商-下拉框
    MET_FAC_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'电能表厂商')]/../div/div/img)[1]")
    # 电能表厂商
    MET_FAC = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'ABB公司')]/../div[contains(text(),'%s')]")
    # 日期
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[1]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("metCheckClockMonth").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[1]/div/div)[1]")


# 电表时钟日统计
class MetClockDayStaticLocators:
    # 【查询条件】
    # 供电单位
    ORG_NO = (
        By.XPATH, ("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 电表类别-下拉框
    MET_TYPE_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'电表类别')]/../div/div/img)[2]")
    # 电表类别
    MET_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'有功表')]/../div[contains(text(),'%s')]")
    # 电能表厂商-下拉框
    MET_FAC_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'电能表厂商')]/../div/div/img)[2]")
    # 电能表厂商
    MET_FAC = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'ABB公司')]/../div[contains(text(),'%s')]")
    # 日期
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[2]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementsByTagName("input")[17].removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (
        By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")


# 电表时钟明细
class MetClockDetailLocators:
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
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'电表类别')]/../div/div/img)[2]")
    # 电表类别
    MET_TYPE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'有功表')]/../div[contains(text(),'%s')]")
    # 电能表资产号
    METER_ASSET_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'电能表资产号')]/../div/input")
    # 用户编号
    CONS_NO = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'用户编号')]/../div/input")
    # 偏差范围-下拉框
    OFFSET_RANGE_SEL = (
        By.XPATH, "//div[@ class =\"x-form-item \"]//*[contains(text(),'偏差范围')]/../div/div/img")
    # 偏差范围
    OFFSET_RANGE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'1分钟-4分钟')]/../div[contains(text(),'%s')]")
    # 终端地址
    TMNL_ADDR = (
        By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'终端地址')]/../div/input")
    # 日期
    QUERY_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[2]/../div/div/input")

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH,
                 "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("metClockDetailMonth").removeAttribute("readonly");'

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
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'1')])[1]/../div[text()='%s']")
    # 周期内自动对时次数-下拉框
    AUTO_TIMES_SEL = (
        By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'周期内自动对时次数')]/../div/div/img)[1]")
    # 周期内自动对时次数
    AUTO_TIMES = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'1')])[2]/../div[text()='%s']")
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


# 电表手工对时
class MetManualCheckLocators:
    # 【查询条件】
    # 节点
    NODE = '后续通过选择电表'
