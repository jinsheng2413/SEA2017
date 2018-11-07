# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesManage_locators.py
@time: 2018/8/29 0029 13:51
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.archivesManage_locators import ArchivesManage_locators


class ArchivesManage_pages(Page):

    # 用户类型
    def inputSel_user_cata(self, index):
        self.click(*ArchivesManage_locators.QRY_USER_CATA)
        locator = self.get_select_locator(ArchivesManage_locators.QRY_USER_CATA_VALUE, index)
        # print(locator)
        self.click(*locator)

    # 户号
    def inputStr_family_no(self, value):
        self.input(value, *ArchivesManage_locators.QRY_FAMILY_NO)

    # 终端资产号
    def inputStr_terminal_asset(self, value):
        self.input(value, *ArchivesManage_locators.QRY_TERMINAL_ASSET_NO)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value, *ArchivesManage_locators.QRY_TERMINAL_ADDR)

    # 【操作区】
    def btn_qry(self):
        self.click(*ArchivesManage_locators.BTN_QRY)

    # 返回菜单
    def btn_menu(self):
        self.click(*ArchivesManage_locators.BTN_MENU)

    # 确定
    def btn_confirm(self):
        self.click(*ArchivesManage_locators.BTN_CONFIRM)

    # 终端资产号明细
    def btn_terminal_asset_detail(self):
        self.click(*ArchivesManage_locators.TAB_ONE_TERMINAL_ASSET_NO_DETAIL)

    # 用户编号明细
    def btn_user_no_detail(self):
        self.click(*ArchivesManage_locators.TAB_ONE_USER_CATA_DETAIL)
