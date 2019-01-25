# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: runTmnlStatistics_locators.py
@time: 2018/10/25 9:24
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→采集建设情况→运行终端统计
class RunTmnlStatisticsLocators:
    # 终端运行状态统计
    # 用户类型
    CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/input')
    # 用户类型→值
    CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 统计日期
    DATE = (By.XPATH, '//label[contains(text(),"统计日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
    # 终端运行状态明细
    # 用户类型
    DETAIL_CONS_TYPE = (
        By.XPATH, '(//label[contains(text(),"用户类型")])[2]/../div/div/input')
    # 用户类型→值
    DETAIL_CONS_TYPE_VALUE = (
        By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端类型
    DETAIL_TMNL_TYPE = (
        By.XPATH, '//label[contains(text(),"终端类型")]/../div/div/input')
    # 终端类型→值
    DETAIL_TMNL_TYPE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 通讯规约
    DETAIL_TMNL_PROTOCOL = (
        By.XPATH, '//label[contains(text(),"通讯规约")]/../div/div/input')
    # 通讯规约→值
    DETAIL_TMNL_PROTOCOL_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 通讯方式
    DETAIL_TMNL_PURPOSE = (
        By.XPATH, '//label[contains(text(),"通讯方式")]/../div/div/input')
    # 通讯方式→值
    DETAIL_TMNL_PURPOSE_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 终端厂家
    DETAIL_TMNL_FACTORY = (
        By.XPATH, '//label[contains(text(),"终端厂家")]/../div/div/input')
    # 终端厂家→值
    DETAIL_TMNL_FACTORY_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 终端状态
    DETAIL_TMNL_STATUS = (
        By.XPATH, '//label[contains(text(),"终端状态")]/../div/div/input')
    # 终端状态→值
    DETAIL_TMNL_STATUS_VALUE = (
        By.XPATH, '(//div[@class="x-combo-list-inner"])[6]/div[%s]')
    # 查询按钮
    BTN_DETAIL_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS操作】
    # 统计日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
