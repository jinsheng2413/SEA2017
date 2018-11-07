# -*- coding: utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: recordsQuery_locators.py
@time: 2018/10/26 16:07
@desc:
'''

from selenium.webdriver.common.by import By

# 高级应用→智能锁具→记录查询
class RecordsQueryLocators:
#开关锁操作日志
    #操作员名称
    STAFF_NAME = (By.XPATH,'//label[contains(text(),"操作员名称")]/../div/div/input')
    #台区编号
    TG_NO = (By.XPATH,'//label[contains(text(),"台区编号")]/../div/div/input')
    #台区名称
    TG_NAME = (By.XPATH,'//label[contains(text(),"台区名称")]/../div/div/input')
    #用户编号
    CONS_NO = (By.XPATH,'//label[contains(text(),"用户编号")]/../div/div/input')
    #用户名称
    USER_NAME = (By.XPATH,'//label[contains(text(),"用户名称")]/../div/div/input')
    # 用户类型
    CONS_TYPE = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/input')
    # 用户类型→值
    CONS_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    #操作行为
    OPERANT_HEHAVIOR = (By.XPATH,'//label[contains(text(),"操作行为")]/../div/div/input')
    #操作行为→值
    OPERANT_HEHAVIOR_VALUE = (By.XPATH,'(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    #操作结果
    OPERANT_RESULT = (By.XPATH,'//label[contains(text(),"操作结果")]/../div/div/input')
    #操作结果→值
    OPERANT_RESULT_VALUE = (By.XPATH,'(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    #电子钥匙编号
    KEY_NO = (By.XPATH,'//label[contains(text(),"电子钥匙编号")]/../div/div/input')
    #锁封编号
    LOCK_NO = (By.XPATH,'//label[contains(text(),"锁封编号")]/../div/div/input')
    #开始日期
    START_DATE = (By.XPATH,'//label[contains(text(),"开始日期")]/../div/div/input')
    #结束日期
    END_DATE = (By.XPATH,'//label[contains(text(),"结束日期")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')
#资产管理记录查询
    #操作员名称
    TAB_STAFF_NAME = (By.XPATH,'(//label[contains(text(),"操作员名称")]/../div/div/input)[2]')
    #电子钥匙编号
    TAB_KEY_NO = (By.XPATH,'(//label[contains(text(),"电子钥匙编号")]/../div/div/input)[2]')
    #锁封编号
    TAB_LOCK_NO = (By.XPATH,'(//label[contains(text(),"锁封编号")]/../div/div/input)[2]')
    #锁封用户编号
    TAB_LOCK_USER_NO = (By.XPATH,'//label[contains(text(),"锁封用户编号")]/../div/div/input')
    #开始日期
    TAB_START_DATE = (By.XPATH,'(//label[contains(text(),"开始日期")]/../div/div/input)[2]')
    #结束日期
    TAB_END_DATE = (By.XPATH,'(//label[contains(text(),"结束日期")]/../div/div/input)[2]')
    # 查询按钮
    TAB_BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

#【JS操作】
    #开关锁操作日志,开始日期，删除readnoly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
    #开关锁操作日志,开始日期，删除readnoly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[15].removeAttribute("readonly");'
    #资产管理记录查询,开始日期，删除readnoly属性
    TAB_START_DATE_JS = 'document.getElementsByTagName("input")[23].removeAttribute("readonly");'
    #资产管理记录查询,开始日期，删除readnoly属性
    TAB_END_DATE_JS = 'document.getElementsByTagName("input")[24].removeAttribute("readonly");'

#【校验区】
    #开关锁操作日志，第一行数据
    CHECK_FIRST = (By.XPATH,'//div[@class="x-grid3-row  x-grid3-row-first "]')
    #资产管理记录查询，第一行数据
    TAB_CHECK_FIRST = (By.XPATH,'(//div[@class="x-grid3-scroller"])[2]/div/div[1]')
