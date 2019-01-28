# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: tmnlInsertQuery_page.py
@time: 2018/11/7 0007 14:59
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询-->报表管理-->国网报表-->智能电能表及终端设备接入情况
class TmnlInsertQueryPage(Page):

    # 统计分类
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 终端厂家
    def inputSel_tmnl_factory(self, options):
        self.selectDropDown(options)

    # 统计口径
    def inputSel_stat_scope(self, option):
        self.selectDropDown(option)

    # 终端类型
    def inputSel_tmnl_type(self, options):
        self.selectDropDown(options)

    # 日期
    def inputDt_dt_from(self, value):
        self.inputDate(value)

    # 到
    def inputDt_dt_to(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
