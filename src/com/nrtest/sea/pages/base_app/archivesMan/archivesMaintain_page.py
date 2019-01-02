# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesMaintain_locators.py
@time: 2018/8/30 0030 14:43
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.archivesMaintain_locators import ArchivesMaintain_locators


# 档案维护
class ArchivesMaintain_pages(Page):
    # 【菜单】
    # 厂站维护
    def btn_menuFactoryMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_FACTORY_MAINTAIN)

    # 终端维护
    def btn_menuTerminalMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_TERMINAL_MAINTAIN)

    # 电表维护
    def btn_menuMeterMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_METER_MAINTAIN)

    # 【查询名称】
    # 厂站名称
    def inputSel_factoryNmae(self, index):
        self.click(ArchivesMaintain_locators.QRY_FACTORY_NAME)
        locator = self.get_select_locator(
            ArchivesMaintain_locators.QRY_FACTORY_NAME_VALUE, index)
        # print(locator)
        self.click(locator)

    # 电压等级
    def inputStr_eleGrade(self, index):
        self.click(ArchivesMaintain_locators.QRY_ELE_GRADE)
        locator = self.get_select_locator(
            ArchivesMaintain_locators.QRY_ELE_GRADE_VALUE, index)
        # print(locator)
        self.click(locator)

    # 终端资产号
    def inputStr_termainalAssetNo(self, value):
        self.input(value, *ArchivesMaintain_locators.QRY_TERMINAL_ASSET_NO)

    # 终端地址
    def inputStr_termainalAddr(self, value):
        self.input(value, *ArchivesMaintain_locators.QRY_TERMINAL_ADDR)

    def btn_factoryQry(self):
        self.click(ArchivesMaintain_locators.BTN_FACTORY_QRY)

    def btn_terminalQry(self):
        self.click(ArchivesMaintain_locators.BTN_TERMINAL_QRY)

    def btn_meterQry(self):
        self.click(ArchivesMaintain_locators.BTN_METER_QRY)


class ArchivesMaintain_factory_pages(Page):
    # 【菜单】
    # 厂站维护
    def btn_menuFactoryMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_FACTORY_MAINTAIN)

    # 终端维护
    def btn_menuTerminalMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_TERMINAL_MAINTAIN)

    # 电表维护
    def btn_menuMeterMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_METER_MAINTAIN)

    # 电压等级
    def inputSel_eleGrade(self, index):
        self.click(ArchivesMaintain_locators.QRY_ELE_GRADE)
        locator = self.get_select_locator(
            ArchivesMaintain_locators.QRY_ELE_GRADE_VALUE, index)
        # print(locator)
        self.click(locator)

    def btn_factoryQry(self):
        self.click(ArchivesMaintain_locators.BTN_FACTORY_QRY)


class ArchivesMaintain_terminal_pages(Page):
    # 【菜单】
    # 厂站维护
    def btn_menuFactoryMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_FACTORY_MAINTAIN)

    # 终端维护
    def btn_menuTerminalMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_TERMINAL_MAINTAIN)

    # 电表维护
    def btn_menuMeterMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_METER_MAINTAIN)

    # 【查询名称】
    # 厂站名称
    def inputSel_factoryNmae(self, index):
        self.click(ArchivesMaintain_locators.QRY_FACTORY_NAME)
        locator = self.get_select_locator(
            ArchivesMaintain_locators.QRY_FACTORY_NAME_VALUE, index)
        # print(locator)
        self.click(locator)

    def btn_terminalQry(self):
        self.click(ArchivesMaintain_locators.BTN_TERMINAL_QRY)


class ArchivesMaintain_meter_pages(Page):
    # 【菜单】
    # 厂站维护
    def btn_menuFactoryMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_FACTORY_MAINTAIN)

    # 终端维护
    def btn_menuTerminalMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_TERMINAL_MAINTAIN)

    # 电表维护
    def btn_menuMeterMaintain(self):
        self.click(ArchivesMaintain_locators.BTN_MENU_METER_MAINTAIN)

    # 【查询名称】

    # 终端资产号
    def inputStr_termainalAssetNo(self, value):
        self.input(value, *ArchivesMaintain_locators.QRY_TERMINAL_ASSET_NO)

    # 终端地址
    def inputStr_termainalAddr(self, value):
        self.input(value, *ArchivesMaintain_locators.QRY_TERMINAL_ADDR)

    def btn_meterQry(self):
        self.click(ArchivesMaintain_locators.BTN_METER_QRY)
