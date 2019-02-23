# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: distributedEnergyAnomalyAnalysis_page.py
@time: 2018/11/9 15:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→重点用户监测→分布式电源管理→分布式电源异常分析
class DistributedEnergyAnomalyAnalysisPage(Page):
    # 查询类型
    def inputChk_qry_type(self, index):
        self.clickRadioBox(index)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 发电类型
    def inputSel_gc_type(self, index):
        self.selectDropDown(index)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

# 高级应用→重点用户监测→分布式电源管理→分布式电源异常分析→分布式电源异常情况明细
class DistributedEnergyAnomalyDetailPage(Page):
    # 查询类型
    def inputChk_qry_type(self, index):
        self.clickRadioBox(index, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 异常类型
    def inputStr_except_type(self, index):
        self.selectDropDown(index)

    # 发电类型
    def inputSel_gc_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 发电量消纳方式
    def inputSel_abso_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
