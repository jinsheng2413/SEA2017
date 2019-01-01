# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: LineDataQueryPage.py
@time: 2018-08-17 13:30
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.lineDataQuery_locators import LineDataQueryLocators


# 统计查询→综合查询→线路数据查询
class LineDataQueryPage(Page):
    # 页面元素
    # 线路编号
    def inputStr_linenum(self, content):
        self.input(content, *LineDataQueryLocators.QRY_LINENUM)

    # 查询按钮
    def btn_search(self):
        self.click(LineDataQueryLocators.BTN_SEARCH)

    # 操作对象选择区
    # 电网结构
    def inputNode_electricpower(self):
        self.click(LineDataQueryLocators.TREE_ELECTRICPOWER)

    # 营销电网结构
    def inputNode_marketing(self):
        self.click(LineDataQueryLocators.TREE_MARKETING)

    # 国网冀北电力有限公司
    def inputNode_jibei(self):
        self.click(LineDataQueryLocators.TREE_JIBEI)

    # 电网_安各庄变电站
    def inputNode_angezhuang(self):
        self.click(LineDataQueryLocators.TREE_ANGEZHUANG)

    # 电网_10kV523安变无税庄
    def inputNode_anbianwu(self):
        self.click(LineDataQueryLocators.TREE_ANBIANWU)

    # 数据展示
    # 查询日期_开始
    def inputdt_starttime(self, value):
        self.input(value)#, *LineDataQueryLocators.INPUTDT_STARTTIME)

    # 查询日期_结束
    def inputdt_endtime(self, value):
        self.input(value)#, *LineDataQueryLocators.INPUTDT_ENDTIME)

    # 查询按钮
    def btn_data_search(self):
        # self.click(LineDataQueryLocators.BTN_DATA_SEARCH)
        self.btn_query()