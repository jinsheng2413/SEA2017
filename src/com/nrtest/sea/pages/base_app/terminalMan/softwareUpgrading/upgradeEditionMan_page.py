# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEditionMan_page.py
@time: 2018/9/25 16:48
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→软件升级→升级版本管理:终端版本信息登记
class UpgradeEditionManPage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index)

    # 软件版本号
    def inputSel_software_version_no(self, option):
        self.selectDropDown(option, byImg=False)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 基本应用→终端管理→软件升级→升级版本管理:终端版本召测
class UpgradeEditionManCallPage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端规约
    def inputSel_tmnl_protocol(self, index):
        self.selectDropDown(index)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 基本应用→终端管理→软件升级→升级版本管理:升级版本管理
class UpgradeEditionManUpPage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

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
        self.btn_query(True)
