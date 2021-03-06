# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: dataStrategyManagenment_page.py
@time: 2018/11/20 0020 14:21
@desc:
"""
from com.nrtest.common.base_page import Page


# 系统管理→数据清理管理→历史数据策略管理
class DataStrategyManagenmentPage(Page):

    # 存储周期
    def inputSel_storage_cycle(self, options):
        self.selectDropDown(options)

    # 表名称
    def inputStr_table_name(self, value):
        self.input(value)

    # 数据组
    def inputSel_data_group(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
