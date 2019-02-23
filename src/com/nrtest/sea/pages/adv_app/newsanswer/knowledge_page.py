# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: knowledge_page.py
@time: 2018-11-02 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class Knowledge_Page(Page):
    # 文件类型
    def inputSel_file_type(self, options):
        self.selectDropDown(options)

    # 文件名称
    def inputStr_file_name(self, value):
        self.input(value)

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
