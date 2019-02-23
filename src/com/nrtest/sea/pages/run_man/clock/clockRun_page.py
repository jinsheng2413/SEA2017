# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: clockRun_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→时钟管理→时钟运行质量分析
# 按单位统计
class StaticByOrgPage(Page):

    # 终端厂商--打开并选择
    def inputSel_tmnl_factory(self, item):
        self.selectDropDown(item)

    # 电能表厂商--打开并选择
    def inputSel_meter_factory(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()

# 按厂家统计
class StaticByFacPage(Page):

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)

# 频繁对时终端
class FrequentlyCheckTmnlPage(Page):

    # 终端类型--打开并选择
    def inputSel_tmnl_type(self, item):
        self.selectDropDown(item)

    # 终端型号
    def inputStr_tmnl_model(self, value):
        self.input(value)

    # 终端厂商--打开并选择
    def inputSel_tmnl_factory(self, item):
        self.selectDropDown(item, is_multi_tab=True, is_multi_elements=True)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)

# 频繁对时电表
class FrequentlyCheckMetPage(Page):

    # 电能表厂商--打开并选择
    def inputSel_meter_factory(self, item):
        self.selectDropDown(item, is_multi_tab=True, is_multi_elements=True)

    # 电表类别--打开并选择
    def inputSel_met_type(self, item):
        self.selectDropDown(item)

    # 电能表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
