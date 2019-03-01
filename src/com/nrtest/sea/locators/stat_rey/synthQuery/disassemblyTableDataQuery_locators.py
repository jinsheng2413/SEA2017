# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: disassemblyTableDataQuery_locators.py
@time: 2018/10/9 11:07
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→销户和拆表数据查询
class DisassemblyTableDataQueryLocators:
    # 用户名称
    CONS_NAME = (By.XPATH, '//label[contains(text(),"用户名称")]/../div/input')
    # 用户编号
    CONS_NO = (By.XPATH, '//label[contains(text(),"用户编号")]/../div/input')
    # 用户类型
    CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    # 用户类型→值
    CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端地址
    TMNL_ADDR = (By.XPATH, '//label[contains(text(),"终端地址")]/../div/input')
    # 电能表资产号
    METER_ASSET_NO = (
        By.XPATH, '//label[contains(text(),"电能表资产号")]/../div/input')
    # 开始时间
    START_DATE = (By.XPATH, '//label[contains(text(),"起")]/../div/div/input')
    # 结束时间
    END_DATE = (By.XPATH, '//label[contains(text(),"止")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')
    # 曲线类型
    CURVE_TYPE = (By.XPATH, '//input[@name="powerCurTypeComboBox"]/../img')

    # 【JS属性】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[9].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[10].removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//div[@class="x-grid3-body"])[1]/div[1]')

    # 第一行的结果
    FIRST_RESULT = (By.XPATH, '(//div[@class="x-grid3-row-checker"])[1]')
