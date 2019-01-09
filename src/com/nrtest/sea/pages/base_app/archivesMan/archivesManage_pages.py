# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesManage_locators.py
@time: 2018/8/29 0029 13:51
@desc:
"""
from com.nrtest.common.base_page import Page


class ArchivesManage_pages(Page):

    # 用户类型
    def inputSel_user_cata(self, option):
        # self.click(ArchivesManage_locators.QRY_USER_CATA)
        # locator = self.get_select_locator(
        #     ArchivesManage_locators.QRY_USER_CATA_VALUE, index)
        # # print(locator)
        # self.click(locator)
        self.selectDropDown(option)

    # 户号
    def inputStr_family_no(self, value):
        self.input(value)  # , *ArchivesManage_locators.QRY_FAMILY_NO)

    # 终端资产号
    def inputStr_terminal_asset(self, value):
        self.input(value)  #, *ArchivesManage_locators.QRY_TERMINAL_ASSET_NO)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)  # , *ArchivesManage_locators.QRY_TERMINAL_ADDR)

    def btt_qry(self):
        self.btn_query()
