# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEffectStatistics_page.py
@time: 2018/9/29 14:16
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeEffectStatistics_locators import \
    UpgradeEffectStatisticsLocators


# 基本应用→终端管理→软件升级→升级效果统计:终端升级统计
class UpgradeEffectStatisticsPage(Page):
    # 统计方式
    def inputChk_stat_mode(self, index):
        self.clickRadioBox(index)

    # 日期类型
    def inputChk_date_type(self, index):
        self.clickRadioBox(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(UpgradeEffectStatisticsLocators.TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        # self.click(UpgradeEffectStatisticsLocators.UPGRADE_PURPOSE)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.UPGRADE_PURPOSE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        # self.click(UpgradeEffectStatisticsLocators.TMNL_PURPOSE)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.TMNL_PURPOSE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        # self.click(UpgradeEffectStatisticsLocators.TMNL_TYPE)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.TMNL_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级类型
    def inputSel_upgrade_type(self, index):
        # self.click(UpgradeEffectStatisticsLocators.UPGRADE_TYPE)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.UPGRADE_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        # self.exec_script(UpgradeEffectStatisticsLocators.START_DATE_JS)
        # self.input(content, *UpgradeEffectStatisticsLocators.START_DATE)
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        # self.exec_script(UpgradeEffectStatisticsLocators.END_DATE_JS)
        # self.input(content, *UpgradeEffectStatisticsLocators.END_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(UpgradeEffectStatisticsLocators.BTN_SEARCH)
        self.btn_query()


# 基本应用→终端管理→软件升级→升级效果统计：终端升级明细
class UpgradeEffectStatisticsDetailPage(Page):
    #终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_UPGRADE_PURPOSE)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_UPGRADE_PURPOSE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级类型
    def inputSel_upgrade_type(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_UPGRADE_TYPE)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_UPGRADE_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_TMNL_PURPOSE)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_TMNL_PURPOSE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 是否成功
    def inputSel_is_success(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_WHETHER_SUCCESS)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_WHETHER_SUCCESS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_TMNL_TYPE)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_TMNL_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级状态
    def inputSel_upgrade_ststus(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_UPGRADE_STATUS)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_UPGRADE_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 确认状态
    def inputSel_confirm_status(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_phase_code)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_phase_code_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 确认结果
    def inputSel_affirm_result(self, index):
        # self.click(UpgradeEffectStatisticsLocators.DETAIL_AFFIRM_RESULT)
        # locator = self.get_select_locator(
        #     UpgradeEffectStatisticsLocators.DETAIL_AFFIRM_RESULT_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 执行日期
    def inputSel_box_exec_date(self, index):
        # self.click(UpgradeEffectStatisticsLocators.BOX_EXECUTE_DATE)
        if index == 'c':
            self.click(UpgradeEffectStatisticsLocators.BOX_EXECUTE_DATE)
        else:
            pass

    # 确认日期
    def inputSel_box_affirm_date(self, index):
        if index == 'c':
            self.click(UpgradeEffectStatisticsLocators.BOX_AFFIRM_DATE)
        else:
            pass

    # 执行开始日期
    def inputDt_start_date(self, content):
        # self.exec_script(UpgradeEffectStatisticsLocators.DETAIL_START_DATE_JS)
        # self.input(content, *UpgradeEffectStatisticsLocators.DETAIL_START_DATE)
        self.inputDate(content)

    # 执行结束日期
    def inputDt_end_date(self, content):
        # self.exec_script(UpgradeEffectStatisticsLocators.DETAIL_END_DATE_JS)
        # self.input(content, *UpgradeEffectStatisticsLocators.DETAIL_END_DATE)
        self.inputDate(content)

    # 确认开始日期
    def inputDt_affirm_start_date(self, content):
        # self.exec_script(UpgradeEffectStatisticsLocators.AFFIRM_START_DATE_JS)
        # self.input(content, *UpgradeEffectStatisticsLocators.AFFIRM_START_DATE)
        self.inputDate(content)

    # 确认结束日期
    def inputDt_affirm_end_date(self, content):
        # self.exec_script(UpgradeEffectStatisticsLocators.AFFIRM_END_DATE_JS)
        # self.input(content, *UpgradeEffectStatisticsLocators.AFFIRM_END_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        # self.click(UpgradeEffectStatisticsLocators.BTN_DETAIL_SEARCH)
        self.btn_query(True)
