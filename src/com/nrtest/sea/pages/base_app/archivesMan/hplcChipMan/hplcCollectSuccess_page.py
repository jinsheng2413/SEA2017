# -*- coding: utf-8 -*-

"""
@author:郭春彪
@license: (C) Copyright 2019, Nari.
@file: hplcCollectSuccess_page.py
@time: 2019-06-28 09:15
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用-->档案管理-->HPLC管理-->HPLC采集成功率
class HplcCollectSuccess_page(Page):

    # 统计日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

        # 查询

    def btn_qry(self):
        self.btn_query()
