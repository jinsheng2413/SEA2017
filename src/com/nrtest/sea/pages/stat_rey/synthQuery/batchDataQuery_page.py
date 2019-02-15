# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: batchDataQuery_page.py
@time: 2018/9/29 18:10
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→批量数据查询
class BatchDataQueryPage(Page):
    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 采集数据Tab页选择
    def inputChk_tab_name(self, option):
        self.clickTabPage(option)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
