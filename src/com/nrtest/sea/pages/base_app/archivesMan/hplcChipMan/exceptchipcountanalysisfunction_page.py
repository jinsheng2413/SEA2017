# -*- coding: utf-8 -*-"""@author: 郭春彪@license: (C) Copyright 2018, Nari.@file: except_chip_count_analysis_function_page_page.py@time: 2019-06-28 14:09:19@desc:"""from com.nrtest.common.base_page import Page# 基本应用→档案管理→HPLC管理→异常芯片统计分析功能:异常载波芯片统计class ExceptChipCountAnalysisFunction_count_Page(Page):    # 月份    def inputDt_query_date(self, value):        self.inputDate(value,is_multi_tab=True)    # 查询    def btn_qry(self):        self.btn_query(is_multi_tab=True)from com.nrtest.common.base_page import Page# 基本应用→档案管理→HPLC管理→异常芯片统计分析功能:异常载波芯片明细class ExceptChipCountAnalysisFunction_detail_Page(Page):    # 异常类型    def inputSel_except_type(self, option):        self.selectDropDown(option)    # 生成时间从    def inputDt_start_time(self, value):        self.inputDate(value)    # 至    def inputDt_end_time(self, value):        self.inputDate(value,is_multi_tab=True)    # 异常状态    def inputSel_except_stat(self, option):        self.selectDropDown(option)    # 终端地址    def inputStr_tmnl_addr(self, value):        self.input(value)    # 查询    def btn_qry(self):        self.btn_query(is_multi_tab=True)