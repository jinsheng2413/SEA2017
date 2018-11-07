# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEditionMan_page.py
@time: 2018/9/25 16:48
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeEditionMan_locators import \
    UpgradeEditionManLocators


# 基本应用→终端管理→软件升级→升级版本管理
class UpgradeEditionManPage(Page):
    # 终端版本信息登记
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.click(*UpgradeEditionManLocators.TMNL_FACTORY)
        locator = self.get_select_locator(UpgradeEditionManLocators.TMNL_FACTORY_VALUE, index)
        self.click(*locator)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.click(*UpgradeEditionManLocators.TMNL_TYPE)
        locator = self.get_select_locator(UpgradeEditionManLocators.TMNL_TYPE_VALUE, index)
        self.click(*locator)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.click(*UpgradeEditionManLocators.TMNL_PURPOSE)
        locator = self.get_select_locator(UpgradeEditionManLocators.TMNL_PURPOSE_VALUE, index)
        self.click(*locator)

    # # 软件版本号
    # def inputSel_software_version_no(self,index):
    #     self.click(*UpgradeEditionManLocators.SOFTWARE_VERSION_NO)
    #     locator = self.get_select_locator(UpgradeEditionManLocators.SOFTWARE_VERSION_NO_VALUE,index)
    #     self.click(*locator)
    # 查询按钮
    def btn_search(self):
        self.click(*UpgradeEditionManLocators.BTN_SEARCH)

    # 升级版本管理
    # 终端厂家
    def inputSel_upgrade_tmnl_factory(self, index):
        self.click(*UpgradeEditionManLocators.UPGRADE_TMNL_FACTORY)
        locator = self.get_select_locator(UpgradeEditionManLocators.UPGRADE_TMNL_FACTORY_VALUE, index)
        self.click(*locator)

    # 终端类型
    def inputSel_upgrade_tmnl_type(self, index):
        self.click(*UpgradeEditionManLocators.UPGRADE_TMNL_TYPE)
        locator = self.get_select_locator(UpgradeEditionManLocators.UPGRADE_TMNL_TYPE_VALUE, index)
        self.click(*locator)

    # 终端用途
    def inputSel_upgrade_tmnl_purpose(self, index):
        self.click(*UpgradeEditionManLocators.UPGRADE_TMNL_PURPOSE)
        locator = self.get_select_locator(UpgradeEditionManLocators.UPGRADE_TMNL_PURPOSE_VALUE, index)
        self.click(*locator)

    # 申请状态
    def inputSel_upgrade_apply_status(self, index):
        self.click(*UpgradeEditionManLocators.UPGRADE_APPLY_STATUS)
        locator = self.get_select_locator(UpgradeEditionManLocators.UPGRADE_APPLY_STATUS_VALUE, index)
        self.click(*locator)

    # 申请开始日期
    def upgrade_start_date(self, content):
        self.exec_script(UpgradeEditionManLocators.UPGRADE_START_DATE_JS)
        self.input(content, *UpgradeEditionManLocators.UPGRADE_START_DATE)

    # 申请结束日期
    def upgrade_end_date(self, content):
        self.exec_script(UpgradeEditionManLocators.UPGRADE_END_DATE_JS)
        self.input(content, *UpgradeEditionManLocators.UPGRADE_END_DATE)

    # 查询按钮
    def btn_upgrade_search(self):
        self.click(*UpgradeEditionManLocators.BTN_UPGRADE_SEARCH)

    # 终端版本召测
    # 终端厂家
    def inputSel_edition_tmnl_factory(self, index):
        self.click(*UpgradeEditionManLocators.EDITION_TMNL_FACTORY)
        locator = self.get_select_locator(UpgradeEditionManLocators.EDITION_TMNL_FACTORY_VALUE, index)
        self.click(*locator)

    # 终端类型
    def inputSel_edition_tmnl_type(self, index):
        self.click(*UpgradeEditionManLocators.EDITION_TMNL_TYPE)
        locator = self.get_select_locator(UpgradeEditionManLocators.EDITION_TMNL_TYPE_VALUE, index)
        self.click(*locator)

    # 终端用途
    def inputSel_edition_tmnl_purpose(self, index):
        self.click(*UpgradeEditionManLocators.EDITION_TMNL_PURPOSE)
        locator = self.get_select_locator(UpgradeEditionManLocators.EDITION_TMNL_PURPOSE_VALUE, index)
        self.click(*locator)

    # 终端规约
    def inputSel_edition_tmnl_protocol(self, index):
        self.click(*UpgradeEditionManLocators.EDITION_TMNL_PROTOCOL)
        locator = self.get_select_locator(UpgradeEditionManLocators.EDITION_TMNL_PROTOCOL_VALUE, index)
        self.click(*locator)

    # 终端地址
    def inputStr_edition_tmnl_addr(self, content):
        self.input(content, *UpgradeEditionManLocators.EDITION_TMNL_ADDR)

    # 查询按钮
    def btn_edition_search(self):
        self.click(*UpgradeEditionManLocators.BTN_EDITION_SEARCH)
