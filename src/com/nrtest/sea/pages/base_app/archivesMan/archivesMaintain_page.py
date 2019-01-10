# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesMaintain_locators.py
@time: 2018/8/30 0030 14:43
@desc:
"""
from com.nrtest.common.base_page import Page


# 基本应用--》档案管理--》档案维护:厂站维护
class ArchivesMaintain_factory_pages(Page):


    # 电压等级
    def inputSel_volt_code(self, index):
        self.selectDropDown(index)

    def btn_qry(self):
        self.btn_query(True)


# 基本应用--》档案管理--》档案维护：终端维护
class ArchivesMaintain_terminal_pages(Page):

    # 厂站名称
    def inputSel_factory_name(self, option):
        self.selectDropDown(option)

    def btn_qry(self):
        self.btn_query(True)


# 基本应用--》档案管理--》档案维护：电表维护
class ArchivesMaintain_meter_pages(Page):

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_termainal_addr(self, value):
        self.input(value)

    def btn_qry(self):
        self.btn_query(True)
