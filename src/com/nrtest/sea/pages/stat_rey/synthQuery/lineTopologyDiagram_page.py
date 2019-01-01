# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineTopologyDiagram_page.py
@time: 2018/10/8 14:15
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.lineTopologyDiagram_locators import LineTopologyDiagramLocators


# 统计查询→综合查询→线路拓扑图
class LineTopoLogyDiagramPage(Page):
    # 线路名称
    def inputSel_line_name(self, index):
        self.click(LineTopologyDiagramLocators.LINE_NAME)
        locator = self.get_select_locator(
            LineTopologyDiagramLocators.LINE_NAME_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search(self):
        self.click(LineTopologyDiagramLocators.BTN_SEARCH)
