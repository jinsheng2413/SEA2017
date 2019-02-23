# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: origFrameHbaseQuery_page.py
@time: 2018/11/9 0009 15:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理-->采集运维平台-->辅助运维→报文查询
class OrigFrameHbaseQueryPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 报文类型
    def inputSel_message_type(self, name):
        self.selectDropDown(name)

    # 查询时间
    def inputStr_query_time(self, value):
        self.input(value)

    # 从
    def inputDt_start_date(self, value):
        self.inputDate(value)
     # 到
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
