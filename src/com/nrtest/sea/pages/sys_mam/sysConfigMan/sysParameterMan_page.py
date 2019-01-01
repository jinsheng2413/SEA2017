# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysParameterMan_page.py
@time: 2018/11/16 11:29
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统配置管理→系统参数管理
# 系统管理→系统配置管理→系统参数管理→系统基本参数设置
class SysBasicParaSetPage(Page):
    # 参数名称
    def inputSel_para_name(self, options):
        # self.click(SysBasicParaSetLocators.QRY_PARA_NAME)
        # locator = self.get_select_locator(SysBasicParaSetLocators.QRY_PARA_NAME_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 参数 编码
    def inputStr_para_no(self, content):
        self.curr_input(content, is_multi_tab=True, is_multi_elements=True)

    # 参数项名称
    def inputStr_para_item_name(self, content):
        self.curr_input(content, is_multi_tab=True, is_multi_elements=True)

    # 参数项编码
    def inputStr_para_item_no(self, content):
        self.curr_input(content, is_multi_tab=True, is_multi_elements=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 系统管理→系统配置管理→系统参数管理→系统异常参数设置
class SysAbnormalParaSetPage(Page):
    # 参数名称
    def inputSel_para_name(self, options):
        # self.click(SysAbnormalParaSetLocators.QRY_PARA_NAME)
        # locator = self.get_select_locator(SysAbnormalParaSetLocators.QRY_PARA_NAME_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 参数编码
    def inputStr_para_no(self, content):
        self.curr_input(content, is_multi_tab=True, is_multi_elements=True)  # , *SysAbnormalParaSetLocators.QRY_PARA_NO)

    # 参数 项 名称
    def inputStr_para_item_name(self, content):
        self.curr_input(content, is_multi_tab=True, is_multi_elements=True)  # , *SysAbnormalParaSetLocators.QRY_PARA_ITEM_NAME)

    # 参数项编码
    def inputStr_para_item_no(self, content):
        self.curr_input(content, is_multi_tab=True, is_multi_elements=True)  #, *SysAbnormalParaSetLocators.QRY_PARA_ITEM_NO)

    # 查询按钮
    def btn_search(self):
        # self.click(SysAbnormalParaSetLocators.BTN_SEARCH)
        self.btn_query(True)
