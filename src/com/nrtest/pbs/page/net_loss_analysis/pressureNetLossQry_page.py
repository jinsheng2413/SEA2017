# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: pressureNetLossQry_page.py
@time: 2019-03-15 14:37
@desc:
"""
from com.nrtest.common.base_page import Page


# 网损分析→分压网损查询:网损查询
class PressureNetLossQryPage(Page):
    # 区域
    def inputSel_area(self, value):
        self.selectDropDown(value)

    # 时间方案
    def inputChk_date_type(self, value):
        self.clickDt_Tab(value)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # TAB页名称
    def inputChk_tab_name(self, value):
        self.clickTabPage(value)

    #电压等级
    def inputChk_ele_level(self,value):
        self.selectDropDown(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
