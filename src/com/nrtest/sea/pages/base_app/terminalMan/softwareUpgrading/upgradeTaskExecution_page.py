# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeTaskExecution_page.py
@time: 2018/9/28 14:22
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→软件升级→升级任务执行
class UpgradeTaskExecutionPage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
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
        self.input(content)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        self.selectDropDown(index)

    # 升级类型
    def inputSel_upgrade_type(self, index):
        self.selectDropDown(index)

    # 执行状态
    def inputSel_execute_status(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
