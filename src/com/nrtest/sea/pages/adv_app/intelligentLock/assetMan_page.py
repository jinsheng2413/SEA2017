# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: assetMan_page.py
@time: 2018/10/26 13:55
@desc:
'''

from com.nrtest.sea.locators.adv_app.intelligentLock.assetMan_locators import AssetManLocators
from com.nrtest.common.base_page import Page

# 高级应用→智能锁具→资产管理
class AssetManPage(Page):
    # 锁封编号
    def inputStr_lock_no(self,content):
        self.input(content,*AssetManLocators.LOCK_NO)
    # 台区名称
    def inputStr_tg_name(self,content):
        self.input(content,*AssetManLocators.TG_NAME)
    # 用户名称
    def inputStr_user_name(self,content):
        self.input(content,*AssetManLocators.USER_NAME)
    # 用户类型
    def inputSel_cons_type(self,index):
        self.click(*AssetManLocators.CONS_TYPE)
        locator = self.get_select_locator(AssetManLocators.CONS_TYPE_VALUE, index)
        self.click(*locator)
    # 锁封资产状态
    def inputSel_lock_asset_ststus(self,index):
        self.click(*AssetManLocators.LOCK_ASSET_STATUS)
        locator = self.get_select_locator(AssetManLocators.LOCK_ASSET_STATUS_VALUE, index)
        self.click(*locator)
    # 锁封状态
    def inputSel_lock_status(self,index):
        self.click(*AssetManLocators.LOCK_STATUS)
        locator = self.get_select_locator(AssetManLocators.LOCK_STATUS_VALUE, index)
        self.click(*locator)
    # 锁封类型
    def inputSel_lock_type(self,index):
        self.click(*AssetManLocators.LOCK_TYPE)
        locator = self.get_select_locator(AssetManLocators.LOCK_TYPE_VALUE, index)
        self.click(*locator)
    # 查询按钮
    def btn_search(self):
        self.click(*AssetManLocators.BTN_SEARCH)