# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: regularSporadicUpgrade_page.py
@time: 2018/9/26 16:12
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端升级→常规零星升级
class RegularSporadicUpgradePage(Page):
    # 忽略历史版本
    def inputChk_history_version(self, index):
        self.clickSingleCheckBox(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index)

    # 升级版本号
    def inputSel_upgrade_version_no(self, index):
        self.selectDropDown(index)

    # 起始终端地址
    def inputStr_tmnl_addr_start(self, content):
        self.input(content)

    # 结束终端地址
    def inputStr_tmnl_addr_end(self, content):
        self.input(content)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()
