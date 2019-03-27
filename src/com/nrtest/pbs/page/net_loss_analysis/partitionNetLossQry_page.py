# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: partitionNetLossQry_page.py
@time: 2019-03-15 14:22
@desc:
"""

from com.nrtest.pbs.locators.net_loss_analysis.partitionNetLossQry_locators import PartitionNetLossQryLocators
from com.nrtest.pbs.tree.tree_page import TreePBSPage


# 网损分析→分区网损查询:网损查询
class PartitionNetLossQryPage(TreePBSPage):
    # 区域
    def inputSel_area(self, value):
        self.selectDropDown(value)

    # 时间方案
    def inputChk_date_type(self, value):
        self.clickTabPage(value)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # TAB页名称
    def inputChk_tab_name(self, value):
        self.clickTabPage(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
