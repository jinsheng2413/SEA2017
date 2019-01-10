# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulVersionMain_page.py
@time: 2018/11/6 0006 14:26
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理--》采集信道管理--》通信模块管理--》本地通信模块版本信息召测
class CommModulVersionMainPage(Page):
    # 终端类型
    def inputSel_tmnlType(self, options):
        # self.click(CommModulVersionMainLocators.QRY_TMNL_TYPE)
        # locator = self.get_select_locator(CommModulVersionMainLocators.QRY_TMNL_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(options)

    # 终端厂商
    def inputSel_tmnlFactory(self, options):
        # self.click(CommModulVersionMainLocators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(CommModulVersionMainLocators.QRY_TMNL_FACTORY_VALUE, name)
        # self.click(locator)
        self.selectDropDown(options)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)#, *CommModulVersionMainLocators.QRY_TMNL_ADDR)

    # 终端规约
    def inputSel_tmnlProtocol(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        # self.click(CommModulVersionMainLocators.BTN_QRY)
        self.btn_query()