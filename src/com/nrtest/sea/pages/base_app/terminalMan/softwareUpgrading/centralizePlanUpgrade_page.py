# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: centralizePlanUpgrade_page.py
@time: 2018/9/29 10:49
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.centralizePlanUpgrade_locators import \
    CentralizePlanUpgradeLocators


# 基本应用→终端管理→软件升级→集中计划升级:集中计划升级
class UpgradeTaskExecutionPage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index)

    # 开始时间
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束时间
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 批次号
    def inputStr_batch_no(self, content):
        self.input(content)  # , *CentralizePlanUpgradeLocators.BATCH_NO)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 基本应用→终端管理→软件升级→集中计划升级:制定计划
class UpgradeTaskExecutionPage(Page):
    # 制定计划
    # 忽略旧版本号
    def inputChk_history_version(self, index):
        self.clickSingleCheckBox(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 升级版本号
    def inputSel_upgrade_version_no(self, index):
        self.click(CentralizePlanUpgradeLocators.TAB_UPGRADE_VERSION_NO)
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
