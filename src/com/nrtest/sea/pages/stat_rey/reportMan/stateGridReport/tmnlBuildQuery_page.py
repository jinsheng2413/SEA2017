# -*- coding:utf-8 -*-
"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: tmnlBuildQuery_page.py
@time: 2018/11/8 9:12
@desc:
"""
from com.nrtest.common.base_page import Page


# 统计查询→报表管理→国网报表→智能电能表及终端设备建设情况

class TmnlBuildQueryPage(Page):

    # 统计分类
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 查询日期

    def inputDt_start_date(self, value):
        self.inputDate(value)

    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 终端类型
    def inputSel_tmnl_type(self, options):
        self.selectDropDown(options)

    # 终端厂商
    def inputSel_tmnl_factory(self, options):
        self.selectDropDown(options)

    # 统计口径
    def inputSel_stat_mode(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
