# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesGet_page.py
@time: 2018/11/28 0028 13:53
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→电表批量导出（冀北）
class ArchivesGetPage(Page):
    # 户号
    def inputStr_userNO(self, value):
        self.input(value)  # , *ArchivesGetLocators.QRY_CONS_NO)

    # 用户类型
    def inputSel_userType(self, option):
        self.selectDropDown(option)

    # 终端资产号
    def inputStr_tmnlAssetNo(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

        # 查询

    def btn_qry(self):
        self.btn_query()
