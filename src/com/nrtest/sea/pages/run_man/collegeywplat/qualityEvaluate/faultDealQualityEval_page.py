# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: faultDealQualityEval_page.py
@time: 2018/11/12 9:20
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→采集运维平台→故障处理质量评价
# 故障处理质量统计
class FaultDealQualityStaticPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, options):
        self.selectDropDown(options)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()


# 故障处理质量明细
class FaultDealQualityDetailPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, options):
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 流程状态-打开并选择
    def inputSel_flow_status(self, options):
        self.selectDropDown(options)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)


# 人员处理明细
class StaffDealDetailPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, options):
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
