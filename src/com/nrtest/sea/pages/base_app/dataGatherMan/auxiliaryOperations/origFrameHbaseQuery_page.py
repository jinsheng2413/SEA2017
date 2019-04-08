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
    def inputDt_query_time(self, value):
        self.inputDate(value)

    # 从
    def inputSel_start_date(self, name):
        self.selectDropDown(name, byImg=False)
     # 到
    def inputSel_end_date(self, name):
        self.selectDropDown(name, byImg=False)

    # 查询
    def btn_qry(self):
        self.btn_query()
