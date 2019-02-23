# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: assetMan_page.py
@time: 2018/10/26 13:55
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→智能锁具→资产管理
class AssetManPage(Page):
    # 锁封编号
    def inputStr_lock_no(self, content):
        self.input(content)
    # 台区名称

    def inputStr_tg_name(self, content):
        self.input(content)

    # 用户名称
    def inputStr_cons_name(self, content):
        self.input(content)

    #  用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index)

    # 锁封资产状态
    def inputSel_lock_asset_status(self, index):
        self.selectDropDown(index)

    # 锁封状态
    def inputSel_lock_status(self, index):
        self.selectDropDown(index)

    # 锁封类型
    def inputSel_lock_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 高级应用→智能锁具→资产管理→已增电子钥匙列表
class AssetManTabPage(Page):
    # 电子钥匙编号
    def inputStr_key_no(self, index):
        self.input(index)

    # 电子钥匙状态
    def inputSel_key_status(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
