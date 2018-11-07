# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: GatherSuccessRateLocators.py
@time: 2018-09-17 13:30
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→采集质量分析→采集成功率
class GatherSuccessRateLocators:
    # 采集成功率→采集成功率
    # 页面元素
    # 查询日期开始
    START_DATE = (
        By.XPATH, '//label[contains(text(),"开始时间")]/../div/div/input')
    # 查询日期结束
    END_DATE = (By.XPATH, '//label[contains(text(),"结束时间")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')
    # 用户类型
    CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/input')
    # 用户类型→值
    CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 显示区
    # 第一个单位
    BTN_FIRST_UNIT = (By.XPATH, '//a[contains(text(),"唐山供电公司")]')
    # 第一个“更多”按钮
    BTN_FIRST_MORE = (By.XPATH, '(//a[contains(text(),"更多")])[1]')
    # 跳出窗口关闭按钮
    BTN_CLOSE = (
        By.XPATH, '//div[@class="x-window-header x-unselectable x-window-draggable"]/div[1]')
    # 第一个结果的采集成功率
    SHOW_FIRST_STATISTICS = (
        By.XPATH, '(//div[@class="x-grid3-cell-inner x-grid3-col-8"]/a)[1]')

    # 采集成功率→采集成功率统计
    # 采集成功率统计
    BTN_STATISTICS = (By.XPATH, '(//span[contains(text(),"采集成功率统计")])[1]')
    # 页面元素
    # 查询日期
    STATISTICS_DATE = (By.XPATH, '//input[@id="readDate"]')
    # 用户类型
    STATISTICS_CONS_TYPE = (By.XPATH, '//input[@id="readSortTypeCombo"]')
    # 用户类型→值
    STATISTICS_CONS_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 查询按钮
    BTN_STATISTICS_SEARCH = (
        By.XPATH, '//table[@id="readSuccessRateQueryBtn"]')

    # 采集成功率→数据采集成功率明细
    # 数据采集成功率明细
    BTN_DETAIL = (By.XPATH, '(//*[contains(text(),"采集成功率明细")])[1]')
    # 页面元素
    # 查询日期
    DETAIL_DATE = (By.XPATH, '//input[@id="failDetail_statDate"]')
    # 用户类型
    DETAIL_CONS_TYPE = (By.XPATH, '//input[@id="failDetail_consTypeCombox"]')
    # 用户类型→值
    DETAIL_CONS_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 查询按钮
    BTN_DETAIL_SEARCH = (By.XPATH, '//table[@id="gatherFailDetailQueryBtn"]')
    # 未抄数
    BTN_DETAIL_NEVER = (
        By.XPATH, '//div[@class="x-grid3-cell-inner x-grid3-col-13"]/a')

    # 采集成功率→连续抄表失败明细
    # 连续抄表失败明细
    BTN_CONTINUOUS_FALSE = (By.XPATH, '//span[contains(text(),"连续抄表失败明细")]')
    # 页面元素
    # 查询日期
    FALSE_DATE = (
        By.XPATH, '(//label[contains(text(),"日期")]/../div/div/input)[3]')
    # 用户类型
    FALSE_CONS_TYPE = (
        By.XPATH, '(//label[contains(text(),"用户类型")]/../div/div/input)[4]')
    # 用户类型→值
    FALSE_CONS_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 查询按钮
    BTN_FALSE_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')
    # 连续N天抄表失败明细
    BTN_FALSE_DETAIL = (By.XPATH, '//span[contains(text(),"连续N天抄表失败明细")]')
    # 应采集电表明细
    BTN_GATHER_DETAIL = (By.XPATH, '//span[contains(text(),"应采集电表明细")]')

    # 基本应用→数据采集管理→采集质量分析→采集成功率→按时间统计
    # 查询日期，开始
    DATE_START_DATE = (By.XPATH, '//input[@name="msq_startDate"]')
    # 查询日期，结束
    DATE_END_DATE = (By.XPATH, '//input[@name="msq_endDate"]')
    # 用户类型
    DATE_CONS_TYPE = (
        By.XPATH, '(//label[contains(text(),"用户类型")]/../div/div/input)[5]')
    # 用户类型→值
    DATE_CONS_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 查询按钮
    BTN_DATE_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[5]')

    # 【JS属性】
    # 用户类型，删除readonly属性
    CONS_TYPE_JS = 'document.getElementsByName("consSortCombo")[0].removeAttribute("readonly");'
    # 查询日期开始，删除readonly属性
    STARTDATE_JS = 'document.getElementsByTagName("input")[27].removeAttribute("readonly");'
    # 查询日期结束，删除readonly属性
    ENDDATE_JS = 'document.getElementsByTagName("input")[28].removeAttribute("readonly");'
    # 采集成功率统计，用户类型，删除readonly属性
    STATISTICS_CONS_TYPE_JS = 'document.getElementsByName("readSortTypeCombo")[0].removeAttribute("readonly");'
    # 采集成功率统计，查询日期，删除readonly属性
    STATISTICS_DATE_JS = 'document.getElementById("readDate").removeAttribute("readonly");'
    # 采集成功率明细，查询日期，删除readonly属性
    DETAIL_DATE_JS = 'document.getElementById("failDetail_statDate").removeAttribute("readonly");'
    # 采集成功率明细→连续抄表失败明细，查询日期，删除readonly属性
    FALSE_DATE_JS = 'document.getElementsByTagName("input")[65].removeAttribute("readonly");'
    # 按时间统计,查询日期开始，删除readonly属性
    DATE_START_DATE_JS = 'document.getElementsByName("msq_startDate")[0].removeAttribute("readonly");'
    # 按时间统计,查询日期结束，删除readonly属性
    DATE_END_DATE_JS = 'document.getElementsByName("msq_endDate")[0].removeAttribute("readonly");'
    # 按时间统计,用户类型，删除readonly属性
    DATE_CONS_TYPE_JS = 'document.getElementsByTagName("input")[57].removeAttribute("readonly");'

    # 【校验区】
    # 表格数据
    DATA_CHECK = (By.XPATH, '//div[@class=" x-window x-resizable-pinned"]')
    # 采集成功率统计
    STATISTICS_CHECK = (By.XPATH, '//div[contains(text(),"唐山供电公司(直属)")]')
    # 采集成功率明细
    DETAIL_CHECK = (By.XPATH, '(//*[contains(text(),"采集成功率明细")])[2]')
    # 采集成功率明细→第一个结果
    DETAIL_FIRST_CHECK = (By.XPATH, '//table[@class="x-grid3-row-table"]')
    # 采集成功率明细→采集失败明细
    DETAIL_FALSE_CHECK = (By.XPATH, '//label[contains(text(),"采集失败明细")]')
    # 采集成功率明细→连续抄表失败明细
    FALSE_CHECK = (
        By.XPATH, '//td[@class="x-grid3-col x-grid3-cell x-grid3-td-0 x-selectable x-grid3-cell-first "]')
    # 采集成功率明细→连续抄表失败明细→连续N天抄表失败明细
    FALSE_DETAIL_CHECK = (By.XPATH, '//table[@class="x-grid3-row-table"]')
