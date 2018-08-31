# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commonMenu_locators.py
@time: 2018/8/28 0028 13:45
@desc:
'''

from com.nrtest.sea.locators.other.commonMenu_locators import CommonMenu_locators
from com.nrtest.common.base_page import Page
class CommonMenu_page(Page):
    #一级菜单
    def menu_first(self,index):
        index = index + 1
        locator = self.get_select_locator(CommonMenu_locators.MENU_FIRST, index)
        self.click(*locator)


    #二级菜单
    def menu_second(self,index):
        locator = self.get_select_locator(CommonMenu_locators.MENU_SECOND, index)
        self.click(*locator)


    #三级菜单
    def menu_three(self,index):
        locator = self.get_select_locator(CommonMenu_locators.MENU_THREE, index)
        self.click(*locator)


    # 【左边树】
    def btn_plus(self,index):
        locator = self.get_select_locator(CommonMenu_locators.BTN_LEFT_PLUS, index)
        self.click(*locator)

    def btn_company_plus(self, index):
        locator = self.get_select_locator(CommonMenu_locators.BTN_COMPANY_PLUS, index)
        self.click(*locator)

    # 选中省份
    def btn_select_province(self):
        self.click(*CommonMenu_locators.BTN_LEFT_MENU_ELETRIC)

    # 选择公司
    def btn_select_company(self, number):
        lr = self.get_select_locator(CommonMenu_locators.BTN_COMPANY, number)
        print(lr)
        self.click(*lr)

    #点击双向箭头
    def btn_left_arrow(self):
        self.click(*CommonMenu_locators.BTN_LEFT_MENU)
