# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: menu_FourName_Page.py
@time: 2018/7/19 0019 15:12
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.other.menu_four_name_locators import MenuFourNameLocators


class MenuFourNamePage(Page):
    # 右击工作台定制
    def btn_right_menu_four_monitor_cust(self):
        self.rightClick(*MenuFourNameLocators.MONITOR_CUST)
