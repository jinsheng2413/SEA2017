# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: four_meter_general_query_page.py
@time: 2019-03-15 16:53:38
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→多表合一综合查询:档案数据
class FourMeterGeneralQueryPage(Page):
    # 用户状态
    def inputSel_user_status(self, option):
        self.selectDropDown(option)

    # Tab页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询
    def btn_qry(self):
        self.btn_query()
