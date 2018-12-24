# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: remoteCommModulVersionMain_page.py
@time: 2018/11/6 0006 15:08
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.runStatusMonitor.communicationModuleManagement.remoteCommModulVersionMain_locators import \
    RemoteCommModulVersionMainLocators


# 运行管理--》采集信道管理--》通信模块管理--》远程通信模块版本信息召测
class RemoteCommModulVersionMainPage(Page):
    # 终端类型
    def inputSel_tmnlType(self, options):
        # self.click(*RemoteCommModulVersionMainLocators.QRY_TMNL_TYPE)
        # locator = self.get_select_locator(RemoteCommModulVersionMainLocators.QRY_TMNL_TYPE_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options)

    # 终端厂商
    def inputSel_tmnlFactory(self, options):
        # self.click(*RemoteCommModulVersionMainLocators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(RemoteCommModulVersionMainLocators.QRY_TMNL_FACTORY_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(options)

    # 终端地址
    def inputStr_tmnlAddr(self, value):
        self.input(value)#, *RemoteCommModulVersionMainLocators.QRY_TMNL_ADDR)

    # 终端资产号
    def inputStr_tmnlAssetNo(self, value):
        self.input(value)#, *RemoteCommModulVersionMainLocators.QRY_TMNL_ASSET_NO)

    # 查询
    def btn_qry(self):
        #self.click(*RemoteCommModulVersionMainLocators.BTN_QRY)
        self.btn_query()
