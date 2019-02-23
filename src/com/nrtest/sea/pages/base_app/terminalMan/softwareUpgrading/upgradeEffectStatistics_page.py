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
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级类型
    def inputSel_upgrade_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 基本应用→终端管理→软件升级→升级效果统计：终端升级明细
class UpgradeEffectStatisticsDetailPage(Page):
    #终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级类型
    def inputSel_upgrade_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 是否成功
    def inputSel_is_success(self, index):
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 升级状态
    def inputSel_upgrade_status(self, index):
        self.selectDropDown(index)

    # 确认状态
    def inputSel_confirm_status(self, index):
        self.selectDropDown(index)

    # 确认结果
    def inputSel_confirm_result(self, index):
        self.selectDropDown(index)

    # 执行日期
    def inputSel_box_exec_date(self, index):
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
        self.inputDate(content)

    # 执行结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 确认开始日期
    def inputDt_affirm_start_date(self, content):
        self.inputDate(content)

    # 确认结束日期
    def inputDt_affirm_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)
