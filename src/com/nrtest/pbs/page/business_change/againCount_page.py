# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: againCount_page.py
@time: 2019-03-14 13:59
@desc:
"""
from com.nrtest.pbs.locators.business_change.againCount_locators import AgainCountLocators
from com.nrtest.pbs.tree.tree_page import TreePBSPage


# 业务变更→重计算
class AgainCountPage(TreePBSPage):
    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # Tab页名称
    def inputChk_tab_name(self, value):
        self.clickTabPage(value, is_by_js=True)

    # 提交按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
