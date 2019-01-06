# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesAnalysisOfAnomaly_locators.py
@time: 2018/8/29 0029 15:56
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.archivesAnalysisOfAnomaly_locators import *


class ArchivesAnalysisOfAnomaly_count_pages(Page):
    # 【菜单】
    # 档案异常明细
    def btn_menu_archives_anomals_detail(self):
        self.click(ArchivesAnalysisOfAnomaly_count_locators.BTN_MENU_ARCHIVES_ABNOLMAL_DETAIL)

    # 档案异常统计
    def btn_menu_archives_anomals_count(self):
        self.click(ArchivesAnalysisOfAnomaly_count_locators.BTN_MENU_ARCHIVES_ABNOLMAL_COUNT)

    # 用户类型
    def inputSel_user_cata(self, index):
        self.click(ArchivesAnalysisOfAnomaly_count_locators.QRY_USER_CATA)
        locator = self.get_select_locator(ArchivesAnalysisOfAnomaly_count_locators.QRY_USER_CATA_VALUE, index)
        self.click(locator)

    # 日期
    def inputStr_date(self, value):
        self.input(value, *ArchivesAnalysisOfAnomaly_count_locators.QRY_DATE)

    # 【操作区】
    def btn_qry(self):
        self.click(ArchivesAnalysisOfAnomaly_count_locators.BTN_QRY)

    # 【显示区】

    # 用户档案异常数
    def btn_user_archives_anomalaum(self):
        self.click(ArchivesAnalysisOfAnomaly_count_locators.TAB_ONE_USER_ARCHIVES_ANOMALS_NUM)

    # 电表档案异常数
    def btn_meter_archives_anomalaum(self):
        self.click(ArchivesAnalysisOfAnomaly_count_locators.TAB_ONE_METER_ARCHIVES_ANOMALS_NUM)

    # 终端档案异常数
    def btn_termianal_archives_anomalaum(self):
        self.click(ArchivesAnalysisOfAnomaly_count_locators.TAB_ONE_TERMIANAL_ARCHIVES_ANOMALS_NUM)


class ArchivesAnalysisOfAnomaly_detail_pages(Page):
    # 【菜单】
    def btn_los(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.BTN_LOS)

    # 档案异常分析
    def btn_menu_anchives_al(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.BTN_MENU_ARCHIVES_ABNOLMAL_AL)

    # 确定
    def btn_confirm(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.BTN_CONFIRM)

    # 档案异常明细
    def btn_menu_archives_anomals_detail(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.BTN_MENU_ARCHIVES_ABNOLMAL_DETAIL)

    # 档案异常统计
    def btn_menu_archives_anomals_count(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.BTN_MENU_ARCHIVES_ABNOLMAL_COUNT)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.QRY_USER_CATA)
        locator = self.get_select_locator(
            ArchivesAnalysisOfAnomaly_detail_locators.QRY_USER_CATA_VALUE, index)
        self.click(locator)

    # 日期
    def inputStr_date(self, value):
        self.input(value, *ArchivesAnalysisOfAnomaly_detail_locators.QRY_DATE)

    # 档案类型
    def inputRSel_archives_cata(self, index):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.QRY_ARCHIVES_CATA)
        locator = self.get_select_locator(
            ArchivesAnalysisOfAnomaly_detail_locators.QRY_ARCHIVES_CATA_VALUE, index)
        self.click(locator)

    # 【操作区】
    def btn_qry(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.BTN_QRY)

    # 【显示区】

    # 用户编号
    def btn_user_no_detail(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.TAB_ONE_USER_NO_DETAIL)

    # 终端资产号
    def btn_terminal_asset_no_detail(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.TAB_ONE_TERMINAL_ASSET_NO_DETAIL)

    # 异常明细
    def btnAnomalsDetail(self):
        self.click(ArchivesAnalysisOfAnomaly_detail_locators.TAB_ABNOLMAI_DETAIL)
