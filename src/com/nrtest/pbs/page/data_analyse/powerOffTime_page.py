# -*- coding: utf-8 -*-"""@author: 邵茜@license: (C) Copyright 2018, Nari.@file: powerOffTime_page.py@time: 2019-03-11 15:03:34@desc:"""from com.nrtest.common.base_page import Page# 数据分析→停电时间统计class PowerOffTimePage(Page):    # 开始时间    def inputDt_start_date(self, value):        self.inputDate(value)    # 结束时间    def inputDt_end_date(self, value):        self.inputDate(value)    # 查询    def btn_qry(self):        self.btn_query(is_multi_tab=True)