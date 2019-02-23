# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: unControlPlantGatherMon_page.py
@time: 2018-11-06 14:46
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用--重点用户监测--非统调电厂管理--非统调电厂采集监测

# 第一个tab页
class UnControlPlantGatherMon1_Page(Page):
    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 发电方式
    def inputSel_gc_type(self, options):
        self.selectDropDown(options)

    # 采集方式
    def inputSel_coll_mode(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 第二个tab页
class UnControlPlantGatherMon2_Page(Page):
    # 发电方式
    def inputSel_gc_type(self, options):
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 采集方式
    def inputSel_coll_mode(self, options):
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 表资产编号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
