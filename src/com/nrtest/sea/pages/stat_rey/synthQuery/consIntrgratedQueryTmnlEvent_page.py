# -*- coding: utf-8 -*-"""@author: 韩笑@license: (C) Copyright 2018, Nari.@file: consIntrgratedQueryTmnlEvent_page.py@time: 2019-02-26 16:03:35@desc:"""from com.nrtest.common.base_page import Page# 统计查询→综合查询→单户综合查询:终端事件class ConsIntrgratedQueryTmnlEventPage(Page):    # 开始日期    def inputDt_start_date(self, value):        self.inputDate(value)    # 结束日期    def inputDt_end_date(self, value):        self.inputDate(value)    # 查询    def btn_qry(self):        self.btn_query(True)