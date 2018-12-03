# -*- coding:utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: base_locators.py
@time: 2018-12-03 14:37
@desc:
"""
from selenium.webdriver.common.by import By


class BaseLocators:
    # 通用查询条件定位
    QRY_INPUT = (By.XPATH, '//label[text()="{}"]/..//input')
    # document.getElementById()、getElementsByName()、getElementsByTagName()

    # 去除查询条件只读属性
    OBJ_JS = 'document.getElementBy{0}("{1}").removeAttribute("readonly");'

    #【下拉复选框相关】
    # 取消所有已选项
    SEL_UNCHECK_ALL = (By.XPATH, '//div[@class ="x-combo-list-inner"]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img')
    # 选择指定复选项
    SEL_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]//div[contains(text(),"{}")]/../div/img')

    # 【下拉单选框相关】
    # 下拉单选项选择
    DROPDOWN_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[contains(text(),"{}")]')