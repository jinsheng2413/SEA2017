# -*- coding: utf-8 -*-"""@author: 邵茜@license: (C) Copyright 2018, Nari.@file: oppAnalyse_page.py@time: 2019-03-11 16:03:34@desc:"""from com.nrtest.pbs.locators.data_analyse.dataApp_locators import DataApp_locatorsfrom com.nrtest.pbs.tree.tree_page import TreePBSPage# 数据分析→对端分析class OppAnalysePage(TreePBSPage):    # 开始时间    def inputDt_start_date(self, value):        self.inputDate(value)    # 结束时间    def inputDt_end_date(self, value):        self.inputDate(value)    # 查询    def btn_qry(self):        self.click(DataApp_locators.BTN_SEARCH)