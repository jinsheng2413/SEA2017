# -*- coding: utf-8 -*-"""@author: 邵茜@license: (C) Copyright 2018, Nari.@file: eleDataQuery_page.py@time: 2019-03-12 09:13:19@desc:"""from com.nrtest.pbs.locators.data_rey.dataRey_locators import DataRey_locatorsfrom com.nrtest.pbs.tree.tree_page import TreePBSPage# 数据查询→电量数据查询class EleDataQueryPage(TreePBSPage):    # 时间方案    def inputChk_time_type(self, option):        self.click_button(option)    # 结束时间    def inputDt_end_date(self, value):        self.inputDate(value)    # 开始时间    def inputDt_start_date(self, value):        self.inputDate(value)    # 查询    def btn_qry(self):        self.click(DataRey_locators.BTN_SEARCH)