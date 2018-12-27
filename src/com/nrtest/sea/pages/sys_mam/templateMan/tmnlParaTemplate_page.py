# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlParaTemplate_page.py
@time: 2018/11/26 15:05
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→模板管理→终端参数模板
class TmnlParaTemplatePage(Page):
    # 终端类型
    def inputSel_tmnl_type(self, option):
        # self.click(*TmnlParaTemplateLocators.QRY_TMNL_TYPE)
        # locator = self.get_select_locator(TmnlParaTemplateLocators.QRY_TMNL_TYPE_VALUE, option)
        # self.click(*locator)
        self.selectDropDown(option)

    # 终端规约
    def inputSel_tmnl_protocol(self, option):
        # self.click(*TmnlParaTemplateLocators.QRY_TMNL_PROTOCOL)
        # locator = self.get_select_locator(TmnlParaTemplateLocators.QRY_TMNL_PROTOCOL_VALUE, option)
        # self.click(*locator)
        self.selectDropDown(option)

    # 查询按钮
    def btn_search(self):
        # self.click(*TmnlParaTemplateLocators.BTN_SEARCH)
        self.btn_query()
