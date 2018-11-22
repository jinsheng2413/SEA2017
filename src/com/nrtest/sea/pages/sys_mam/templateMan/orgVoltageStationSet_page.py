# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: orgVoltageStationSet_page.py
@time: 2018/11/21 11:19
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.templateMan.orgVoltageStationSet_locators import OrgVoltageStationSetLocators


# 系统管理→模板管理→供电电压测点设置
class OrgVoltageStationSetPage(Page):
    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content, *OrgVoltageStationSetLocators.QRY_CONS_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *OrgVoltageStationSetLocators.QRY_TMNL_ADDR)

    # 电表资产
    def inputStr_meter_asset_no(self, content):
        self.input(content, *OrgVoltageStationSetLocators.QRY_METER_ASSET_NO)

    # 注册信息
    def inputSel_login_infor(self, index):
        self.click(*OrgVoltageStationSetLocators.QRY_LOGIN_INFOR)
        locator = self.get_select_locator(OrgVoltageStationSetLocators.QRY_LOGIN_INFOR_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*OrgVoltageStationSetLocators.BTN_SEARCH)
