# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysCoverageQuery_page.py
@time: 2018/11/8 10:34
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→报表管理→国网报表→系统采集覆盖情况
class SysCoverageQueryPage(Page):

    # 统计分类
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 日期
    def inputDt_stat_date(self, stat_date):
        self.inputDate(stat_date)

    # 统计口径
    def inputSel_stat_scope(self, option):
        self.selectDropDown(option)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
