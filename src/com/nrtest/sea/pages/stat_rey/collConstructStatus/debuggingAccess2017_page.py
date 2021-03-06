# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: debuggingAccess2017_page.py
@time: 2018/10/25 16:49
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→采集建设情况→调试接入情况2017
class DebuggingAccess2017Page(Page):
    # 页面元素
    # 管理方式
    def inputSel_manage_style(self, index):
        self.selectDropDown(index)

    # 装接方式
    def inputSel_install_mode(self, index):
        self.selectCheckBox(index)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()
