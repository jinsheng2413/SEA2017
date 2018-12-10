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
    """
    基类Page的元素定义
    """
    # document.getElementById()、getElementsByName()、getElementsByTagName()
    # presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
    # visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。

    # 框定菜单范围
    # '//div[@id="档案查询" and @class =" x-panel x-panel-noborder  x-hide-offsets"]'


    # 通用查询条件定位
    # 与工作台一起的已打开菜单ID  class=" x-panel x-panel-noborder  x-hide-offsets"
    MENU_PAGE_ID = '//div[@id="{}"]'

    # 多个TAB页情况下的元素定位附加内容: '//div[@class =" x-panel x-panel-noborder  x-hide-display"]'
    # 预留
    MULTI_TAB = ''

    # 【输入框】
    # 按标签定位input
    QRY_INPUT = (By.XPATH, '//div[@class="x-form-item "]/label[text()="{}"]/..//input')
    # 按input直接定位
    ATTRS = ['name', 'id']
    QRY_INPUT_BY = (By.XPATH, '//input[@{}="{}"]')  # 如：'//input[@name="{}"]'

    # 【日期等只读属性改变】
    # 去除查询条件只读属性，如：日期选择框
    JS_REMOVE_ATTR = 'document.getElementBy{0}("{1}").removeAttribute("{}");'

    # 【下拉框】
    # 下拉选择点击按钮
    SEL_CHECKBOX = (By.XPATH, '//label[text()="{}"]/..//img')
    SEL_CHECKBOX_BY = (By.XPATH, '//input[@{}="{}"]/../img')


    #【下拉复选框相关】
    # 取消所有已选项
    # SEL_UNCHECK_ALL = (By.XPATH, '//div[@class ="x-combo-list-inner"]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img')
    SEL_UNCHECK_ALL = (By.XPATH,
                       '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img')
    # 选择指定复选项@class="ux-lovcombo-item-text" and
    # SEL_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]//div[contains(text(),"{}")]/../div/img')
    SEL_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/..//img')


    # 【下拉单选框相关】
    # 下拉单选项选择@class="x-combo-list-item" and
    # DROPDOWN_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[contains(text(),"{}")]')
    DROPDOWN_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]')
    # $x('//div[@class="x-layer x-combo-list  x-resizable-pinned" and contains(@style,"visible;")]//div[contains(text(),"巡检仪")]')

    # 【单选框】 by:name\id
    # 根据标签找input
    RADIOBOX_LABEL2INPUT = (
    By.XPATH, '//div[contains(@class,"x-form-radio-group")]//label[@class="x-form-cb-label" and text()="{}"]/../input[@type="radio"]')

    # 根据INPUT的name找标签
    RADIOBOX_INPUT2LABEL = (By.XPATH, '//input[@type="radio" and @name="{}"]/..label[@text()="{}"')
    # 'div[contains(@class,"x-form-radio-group"]'

    # 【复选框】
    # input 有checked=""属性时表示已选中，没有表示未选中 get_attribute
    # 未选择
    CHECKBOX_UNCHECKED = (By.XPATH, '//div[@class="x-form-check-wrap"]//label[@class="x-form-cb-label" and text()="{}"]/../input[@type="checkbox"]')
    # 已选择
    CHECKBOX_CHECKED = (
    By.XPATH, '//div[@class="x-form-check-wrap"]//label[@class="x-form-cb-label" and text()="{}"]/../input[@type="checkbox" and @checked=""]')

    CHECKBOX_CHECKED_BY_INPUT = (By.XPATH, '//input[@type="checkbox" and @checked="" and @name="{}"]')

    # 【按钮类元素】，如：查询按钮
    BTN_QRY = (By.XPATH, '//button[@class =" x-btn-text" and contains(text(),"{}")]')


    # 菜单页面定位{}=远程调试
    MENU_PAGE = (By.XPATH, '//li[@id="maintab__{}"]')

    # 定位一个菜单页面内的某一Tab页
    TAB_PAGE = (By.XPATH, '//span[@class="x-tab-strip-text " and text()={}]')

    # 登录后弹出窗口：账号异常
    BTN_ACCOUNT_EXCEPT = (By.XPATH,
                          '//div[@class="x-window-header x-unselectable x-window-draggable"]/span[@class="x-window-header-text"]/../div[contains(@class,"x-tool-close")]')

    # 登录后弹出窗口：推出重要信息
    BTN_IMPORTANT_INFO = (By.XPATH, '//button[@class=" x-btn-text cancel" and text()="不再提醒"]')
