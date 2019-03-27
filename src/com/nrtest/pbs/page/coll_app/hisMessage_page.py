# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: hisMessage_page.py
@time: 2019-03-11 14:38:37
@desc:
"""
from com.nrtest.common.base_page import Page


# 采集运维→历史报文
class HisMessagePage(Page):
    # 报文时间
    def inputDt_message_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
