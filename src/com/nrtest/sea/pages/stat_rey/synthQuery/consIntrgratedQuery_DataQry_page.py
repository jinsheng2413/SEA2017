# -*- coding: utf-8 -*-"""@author: 卢炎炎@license: (C) Copyright 2018, Nari.@file: consIntrgratedQuery_DataQry_page.py@time: 2019-02-26 14:55:25@desc:"""from com.nrtest.common.base_page import Page# 统计查询→综合查询→单户综合查询:日抄表数据class ConsIntrgratedDayQueryPage(Page):    # 从    def inputDt_start_date(self, value):        self.inputDate(value)    # 到    def inputDt_end_date(self, value):        self.inputDate(value)    # 数据类型    def inputChk_data_type(self, options):        self.clickCheckBox_new(options)    # 查询    def btn_qry(self):        self.btn_query()# 统计查询→综合查询→单户综合查询:实时抄表数据class ConsIntrgratedRealTimeQueryPage(Page):    # 从    def inputDt_start_date(self, value):        self.inputDate(value)    # 到    def inputDt_end_date(self, value):        self.inputDate(value)    # 数据类型    def inputChk_data_type(self, options):        self.clickCheckBox_new(options)    # 查询    def btn_qry(self):        self.btn_query()