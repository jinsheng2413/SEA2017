# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEditionApprove_page.py
@time: 2018/9/27 15:45
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→软件升级→升级版本审批
class UpgradeEditionApprovePage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index)

    # 申请状态
    def inputSel_apply_status(self, index):
        self.selectDropDown(index)

    # 申请开始日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 申请结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
