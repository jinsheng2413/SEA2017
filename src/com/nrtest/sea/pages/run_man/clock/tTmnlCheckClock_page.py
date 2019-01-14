# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→时钟管理→终端对时
# 终端时钟统计
class TmnlClockStaticPage(Page):

    # 终端类型--打开并选择
    def inputSel_tmnl_type(self, item):
        self.selectDropDown(item)

    # 终端厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()

# 终端时钟明细
class TmnlClockDetailPage(Page):

    # 偏差范围--打开并选择
    def inputSel_offset_range(self, item):
        self.selectDropDown(item)

    # 终端类型--打开并选择
    def inputSel_tmnl_type(self, item):
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 终端型号
    def inputStr_tmnl_model(self, value):
        self.input(value)

    # 终端厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 是否在线--打开并选择
    def inputSel_is_online(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 是否历史
    def inputChk_is_history(self, value):
        self.clickSingleCheckBox(value)

    # 对时结果-打开并选择
    def inputSel_call_status(self, item):
        self.selectDropDown(item)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)

# 自动对时策略配置
class AutoCheckPolicyPage(Page):

    # 间隔周期--打开并选择
    def inputSel_interval_cycle(self, item):
        self.selectDropDown(item)

    # 周期内自动对时次数--打开并选择
    def inputSel_auto_times(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
