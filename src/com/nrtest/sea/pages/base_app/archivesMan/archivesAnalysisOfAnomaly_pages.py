# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesAnalysisOfAnomaly_locators.py
@time: 2018/8/29 0029 15:56
@desc:
"""
from com.nrtest.common.base_page import Page


# 档案异常分析_统计
class ArchivesAnalysisOfAnomaly_count_pages(Page):

    # 用户类型
    def inputSel_user_cata(self, option):
        # self.click(ArchivesAnalysisOfAnomaly_count_locators.QRY_USER_CATA)
        # locator = self.get_select_locator(ArchivesAnalysisOfAnomaly_count_locators.QRY_USER_CATA_VALUE, index)
        # self.click(locator)
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)  # , *ArchivesAnalysisOfAnomaly_count_locators.QRY_DATE)

    # 【操作区】
    def btn_qry(self):
        self.btn_query(True)


class ArchivesAnalysisOfAnomaly_detail_pages(Page):

    # 确定
    def btn_qry(self):
        # self.click(ArchivesAnalysisOfAnomaly_detail_locators.BTN_CONFIRM)
        self.btn_query(True)

    # 用户类型
    def inputSel_cons_type(self, option):
        # self.click(ArchivesAnalysisOfAnomaly_detail_locators.QRY_USER_CATA)
        # locator = self.get_select_locator(
        #     ArchivesAnalysisOfAnomaly_detail_locators.QRY_USER_CATA_VALUE, index)
        # self.click(locator)
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)  # , *ArchivesAnalysisOfAnomaly_detail_locators.QRY_DATE)

    # 档案类型
    def inputRSel_archives_cata(self, index):
        # self.click(ArchivesAnalysisOfAnomaly_detail_locators.QRY_ARCHIVES_CATA)
        # locator = self.get_select_locator(
        #     ArchivesAnalysisOfAnomaly_detail_locators.QRY_ARCHIVES_CATA_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True)
