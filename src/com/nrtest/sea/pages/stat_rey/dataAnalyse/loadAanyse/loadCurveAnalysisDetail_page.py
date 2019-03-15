# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: load_curve_analysis_page.py
@time: 2019-03-14 16:38:57
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→数据分析→负荷分析→负荷曲线分析:负荷曲线明细
class LoadCurveAnalysisDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 曲线类型
    def inputSel_curve_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 日期
    def inputDt_qurery_date(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 行业
    def inputSel_industry(self, value):
        self.selectDropDown(value, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
