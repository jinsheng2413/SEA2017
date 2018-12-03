# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesGet_page.py
@time: 2018/11/28 0028 13:53
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.archivesGet_locators import ArchivesGetLocators


# 基本应用--》档案管理--》电表批量导出（冀北）
class ArchivesGetPage(Page):
    # 户号
    def inputStr_userNO(self, value):
        self.input(value, *ArchivesGetLocators.QRY_USER_NO)

    # 用户类型
    def inputSel_userType(self, name):
        self.click(*ArchivesGetLocators.QRY_USER_TYPE)
        locator = self.get_select_locator(ArchivesGetLocators.QRY_USER_TYPE_VALUE, name)
        self.click(*locator)

    # 终端资产号
    def inputStr_tmnlAssetNo(self, value):
        self.input(value, *ArchivesGetLocators.QRY_TMNL_ASSET_NO)

    # 终端地址
    def inputStr_tmnlAddr(self, value):
        self.input(value, *ArchivesGetLocators.QRY_TMNL_ADDR)

        # 查询

    def btn_qry(self):
        self.click(*ArchivesGetLocators.BTN_QRY)