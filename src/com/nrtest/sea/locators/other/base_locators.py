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
    # document.getElementById()、getElementsByName()、getElementsByTagName()

    # 通用查询条件定位
    QRY_INPUT = (By.XPATH, '//label[text()="{}"]/..//input')
    QRY_INPUT_BY_NAME = (By.XPATH, '//input[@name="{}"]')

    # 下拉选择点击按钮
    QRY_CHECK_BOX = (By.XPATH, '//label[text()="{}"]/..//img')
    QRY_CHECK_BOX_BY_NAME = (By.XPATH, '//input[@name="{}"]/../img')

    # 去除查询条件只读属性
    OBJ_JS = 'document.getElementBy{0}("{1}").removeAttribute("readonly");'

    #【下拉复选框相关】
    # 取消所有已选项
    SEL_UNCHECK_ALL = (By.XPATH, '//div[@class ="x-combo-list-inner"]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img')
    # 选择指定复选项@class="ux-lovcombo-item-text" and
    SEL_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]//div[contains(text(),"{}")]/../div/img')

    # 【下拉单选框相关】
    # 下拉单选项选择@class="x-combo-list-item" and
    DROPDOWN_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[contains(text(),"{}")]')

    # 菜单页面定位{}=远程调试
    MENU_PAGE = (By.XPATH, '//li[@id="maintab__{}"]')

    # 一个页面内的Tab页
    TAB_PAGE = (By.XPATH, '//span[@class="x-tab-strip-text " and text()={}]')

    # 登录后弹出窗口：账号异常
    BTN_ACCOUNT_EXCEPT = (By.XPATH,
                          '//div[@class="x-window-header x-unselectable x-window-draggable"]/span[@class="x-window-header-text"]/../div[contains(@class,"x-tool-close")]')

    # 登录后弹出窗口：推出重要信息
    BTN_IMPORTANT_INFO = (By.XPATH, '//button[@class=" x-btn-text cancel" and text()="不再提醒"]')
