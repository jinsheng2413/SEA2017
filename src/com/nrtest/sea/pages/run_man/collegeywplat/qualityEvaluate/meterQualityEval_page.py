# -*- coding:utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: collTmnlQualityEval_page.py
@time: 2018/11/13 9:20
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→采集运维平台→采集终端质量评价
# 电表质量评价统计
class MeterQualityEvalStaticPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, name):
        self.selectDropDown(name)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 电表厂家--打开并选择
    def inputSel_meter_factory(self, name):
        self.selectDropDown(name, is_multi_elements=True, is_multi_tab=True)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)

# 电表质量评价明细
class MeterQualityEvalDetailPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 故障严重程度--打开并选择
    def inputSel_fault_severity(self, name):
        self.selectDropDown(name)

    # 电表厂家-打开并选择
    def inputSel_meter_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 故障类别-打开并选择
    def inputSel_fault_type(self, name):
        self.selectDropDown(name)

    # 故障开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 故障结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
