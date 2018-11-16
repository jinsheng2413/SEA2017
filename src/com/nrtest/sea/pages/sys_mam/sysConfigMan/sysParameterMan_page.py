# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysParameterMan_page.py
@time: 2018/11/16 11:29
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.sysConfigMan.sysParameterMan_locators import *


# 系统管理→系统配置管理→系统参数管理
# 系统管理→系统配置管理→系统参数管理→系统基本参数设置
class SysBasicParaSetPage(Page):
    # 参数名称
    def inputSel_para_name(self, index):
        self.click(*SysBasicParaSetLocators.QRY_PARA_NAME)
        locator = self.get_select_locator(SysBasicParaSetLocators.QRY_PARA_NAME_VALUE, index)
        self.click(*locator)

    # 参数编码
    def inputStr_para_no(self, content):
        self.input(content, *SysBasicParaSetLocators.QRY_PARA_NO)

    # 参数项名称
    def inputStr_para_item_name(self, content):
        self.input(content, *SysBasicParaSetLocators.QRY_PARA_ITEM_NAME)

    # 参数项编码
    def inputStr_para_item_no(self, content):
        self.input(content, *SysBasicParaSetLocators.QRY_PARA_ITEM_NO)

    # 查询按钮
    def btn_search(self):
        self.click(*SysBasicParaSetLocators.BTN_SEARCH)


# 系统管理→系统配置管理→系统参数管理→系统异常参数设置
class SysAbnormalParaSetPage(Page):
    # 参数名称
    def inputSel_para_name(self, index):
        self.click(*SysAbnormalParaSetLocators.QRY_PARA_NAME)
        locator = self.get_select_locator(SysAbnormalParaSetLocators.QRY_PARA_NAME_VALUE, index)
        self.click(*locator)

    # 参数编码
    def inputStr_para_no(self, content):
        self.input(content, *SysAbnormalParaSetLocators.QRY_PARA_NO)

    # 参数项名称
    def inputStr_para_item_name(self, content):
        self.input(content, *SysAbnormalParaSetLocators.QRY_PARA_ITEM_NAME)

    # 参数项编码
    def inputStr_para_item_no(self, content):
        self.input(content, *SysAbnormalParaSetLocators.QRY_PARA_ITEM_NO)

    # 查询按钮
    def btn_search(self):
        self.click(*SysAbnormalParaSetLocators.BTN_SEARCH)
