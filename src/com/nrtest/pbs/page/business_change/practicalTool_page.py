# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: practicalTool_page.py
@time: 2019-07-08 13:58
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.pbs.locators.business_change.practicalTool_locators import PracticalToolLocators


# 业务变更→实用工具:统计相关电表配置
class PracticalToolStatPage(Page):
    # 统计相关电表配置
    def btn_practical_tool_stat(self):
        self.click(PracticalToolLocators.Practical_Tool_Stat)

    # 松原地区
    def btn_tree_song_yuan(self):
        self.click(PracticalToolLocators.Tree_Song_Yuan)

    # 统计类型
    def inputSel_stat_type(self,value):
        self.selectDropDown(value)

    # 是否参与统计
    def inputSel_whether_participate(self,value):
        self.selectDropDown(value)

    # 对象
    def inputSel_query_object(self,value):
        self.selectDropDown(value)

    #查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)

# 业务变更→实用工具:计算公式手动查询
class PracticalToolQueryPage(Page):
    # 计算公式手动查询
    def btn_practical_tool_query(self):
        self.click(PracticalToolLocators.Practical_Tool_Query)

    # 公式
    def inputSel_query_formula(self,value):
        self.selectDropDown(value)

    # 时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)