# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: collStatus_page.py
@time: 2019-07-08 15:07
@desc:
"""

from com.nrtest.common.base_page import Page


# 状态监视→采集状态
class CollStatusPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 数据类型
    def inputChk_data_type(self,value):
        self.clickRadioBox(value)
        
    # 查询按钮
    def btn_qry(self):
        self.btn_query()