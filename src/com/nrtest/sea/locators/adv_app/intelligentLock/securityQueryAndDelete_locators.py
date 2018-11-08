# -*- coding: utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: securityQueryAndDelete_locators.py
@time: 2018/10/29 9:17
@desc:
'''

from selenium.webdriver.common.by import By

# 高级应用→智能锁具→权限查询及删除


class SecurityQueryAndDeleteLocators:
    # 电子钥匙编号
    KEY_NO = (By.XPATH, '//label[contains(text(),"电子钥匙编号")]/../div/div/input')
    # 锁封编号
    LOCK_NO = (By.XPATH, '//label[contains(text(),"锁封编号")]/../div/div/input')
    # 操作员编号
    STAFF_NO = (By.XPATH, '//label[contains(text(),"操作员编号")]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[text()="查询"]')

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
