# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgTopologyDiagram_page.py
@time: 2018/10/9 9:47
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.tgTopologyDiagram_locators import TgTopologyDiagramLocators


# 统计查询→综合查询→台区拓扑图
class TgTopologyDiagramPage(Page):
    # 专公变类型
    def inputSel_tmnl_type(self, index):
        self.click(*TgTopologyDiagramLocators.TMNL_TYPE)
        locator = self.get_select_locator(TgTopologyDiagramLocators.TMNL_TYPE_VALUE, index)
        self.click(locator)

    # 台区编码
    def inputStr_tg_no(self, content):
        self.input(content, *TgTopologyDiagramLocators.TG_NO)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content, *TgTopologyDiagramLocators.TG_NAME)

    # 查询按钮
    def btn_search(self):
        self.click(*TgTopologyDiagramLocators.BTN_SEARCH)
