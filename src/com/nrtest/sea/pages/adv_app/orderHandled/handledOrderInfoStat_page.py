# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: handledOrderInfoStat_page.py
@time: 2019-02-13 9:14
@desc:
'''

# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: handled_order_info_stat_page.py
@time: 2019-02-13 09:12:30
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→工单处理→掌机抄表工单统计（青海）
class HandledOrderInfoStatPage(Page):
    # 查询方式
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 从
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 至
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
