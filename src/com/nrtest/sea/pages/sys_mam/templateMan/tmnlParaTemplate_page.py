# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlParaTemplate_page.py
@time: 2018/11/26 15:05
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.templateMan.tmnlParaTemplate_locators import TmnlParaTemplateLocators


# 系统管理→模板管理→终端参数模板
class TmnlParaTemplatePage(Page):
    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.click(*TmnlParaTemplateLocators.QRY_TMNL_TYPE)
        locator = self.get_select_locator(TmnlParaTemplateLocators.QRY_TMNL_TYPE_VALUE, index)
        self.click(*locator)

    # 终端规约
    def inputSel_tmnl_protocol(self, index):
        self.click(*TmnlParaTemplateLocators.QRY_TMNL_PROTOCOL)
        locator = self.get_select_locator(TmnlParaTemplateLocators.QRY_TMNL_PROTOCOL_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*TmnlParaTemplateLocators.BTN_SEARCH)
