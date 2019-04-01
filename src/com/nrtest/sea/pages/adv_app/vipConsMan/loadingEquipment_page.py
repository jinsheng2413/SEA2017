# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: loadingEquipment_page.py
@time: 2018-11-05 15:53
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→重点用户监测→加载防窃电设备
class LoadingEquipment_Page(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 选择指定行
    def inputRow_select_row(self, row_item):
        self.select_row(row_item)

    # 查询
    def btn_qry(self):
        self.btn_query()
