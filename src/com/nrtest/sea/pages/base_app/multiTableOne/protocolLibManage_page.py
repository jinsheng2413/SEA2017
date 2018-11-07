# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.multiTableOne.protocolLibManage_locators import ProtocolLibManageLocators


# 基本应用--》多表合一--》协议管理

class ProtocolLibManageLocatorsPage(Page):
    # 协议名称
    def inputStr_protocolName(self, value):
        self.input(value, *ProtocolLibManageLocators.QRY_PROTOCOL_NAME)

    # 厂商名称
    def inputStr_manufacturerName(self, value):
        self.input(value, *ProtocolLibManageLocators.QRY_MANUFACTORY_NAME)

    # 协议类型
    def inputStr_protocolType(self, value):
        self.input(value, *ProtocolLibManageLocators.QRY_PROTOCOL_TYPE)

    # 表记类型
    def inputStr_surfaceType(self, value):
        self.input(value, *ProtocolLibManageLocators.QRY_SURFACE_TYPE)

    # 维护时间
    def inputStr_maintenanceTmie(self, value):
        self.input(value, *ProtocolLibManageLocators.QRY_MAINTENANCE_TIME)

    # 结束时间
    def inputStr_endTime(self, value):
        self.input(value, *ProtocolLibManageLocators.QRY_END_TIME)

    # 有效标志
    def inputSel_effectiveSign(self, name):
        self.click(*ProtocolLibManageLocators.QRY_EFFECTIVE_SIGN)
        locator = self.get_select_locator(
            ProtocolLibManageLocators.QRY_EFFECTIVE_SIGN_VALUE, name)
        self.click(*locator)

    # 协议版本号
    def inputStr_protocolVersionNo(self, value):
        self.input(value, *ProtocolLibManageLocators.QRY_PROTOCOL_VERSION_NO)

    # 协议代码
    def inputStr_protocolCode(self, value):
        self.input(value, *ProtocolLibManageLocators.QEY_PROTOCOL_CODE)

    # 查询
    def btn_qry(self):
        self.click(*ProtocolLibManageLocators.BTN_QRY)
