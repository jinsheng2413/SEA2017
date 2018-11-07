# -*- coding: utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: securityControl_locators.py
@time: 2018/10/26 15:33
@desc:
'''

from selenium.webdriver.common.by import By

# 高级应用→智能锁具→权限控制
class SecurityControlLocators:
    #供电单位，查询按钮
    BTN_CONS_SEARCH = (By.XPATH,'(//div[@class="x-column-inner"])[1]//button[text()="查询"]')
    #锁封编号
    LOCK_NO = (By.XPATH,'//label[contains(text(),"锁封编号")]/../div/div/input')
    #用户编号
    CONS_NO = (By.XPATH, '//label[contains(text(),"用户编号")]/../div/div/input')
    #查询按钮
    BTN_SEARCH = (By.XPATH, '(//div[@class="x-column-inner"])[2]//button[text()="查询"]')

#【校验区】
    #第一行数据
    CHECK_FIRST = (By.XPATH,'(//div[@class="x-grid3-body"])[2]/div[1]')
