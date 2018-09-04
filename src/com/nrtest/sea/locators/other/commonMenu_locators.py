# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commonMenu_locators.py
@time: 2018/8/28 0028 13:45
@desc:
'''
from selenium.webdriver.common.by import By
class CommonMenu_locators:
    #一级菜单
    MENU_FIRST =(By.XPATH,"// *[@id =\"menu1\"]/tbody/tr/td[%s]")
    #二级菜单
    MENU_SECOND = (By.XPATH,'//*[@id=\"smenu\"]//*[@class=\"x-toolbar-left-row\"]/td[%s]')
    #三级菜单
    MENU_THREE = (By.XPATH,'//ul[@class=\"x-menu-list\"]/li[%s]')

    # 【左边树】
    # 左边树按钮
    BTN_LEFT_MENU = (By.XPATH, '//*[@id="mainwest-xcollapsed"]/div')
    # 左边树国王冀北店里有限公司
    BTN_LEFT_MENU_ELETRIC = (By.XPATH, '//span[@unselectable="on"]')
    # 菜单下拉框选择
    BTN_MENU = (By.XPATH, '//*[@id="menuUseStat_menuCombo_1"]')
    # 左边加号
    BTN_LEFT_PLUS = (By.XPATH, '(//img[@class=\"x-tree-ec-icon x-tree-elbow-end-plus\"])[%s]')
    #公司加号
    BTN_COMPANY_PLUS = (By.XPATH,'(//img[@class=\"x-tree-ec-icon x-tree-elbow-plus\"])[%s]')
    # 市
    BTN_COMPANY = (By.XPATH, '(//a[@class=\"x-tree-node-anchor\"])[%s]')
    #县
    BTN_COUNTY = (By.XPATH,"//span[contains(text(),'直属用户')]/../../../../li[%s]")
    #县和用户
    BTN_COUNTY_AND_USER = (By.XPATH,"//span[contains(text(),'直属用户')]/../../../../li[%s]/ul/li[%s]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[%s]')
    TAB_TWO = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[%s]')


