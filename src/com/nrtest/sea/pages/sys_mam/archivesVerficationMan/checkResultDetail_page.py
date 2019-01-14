# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: verficationResultDetail_page.py
@time: 2018/11/16 0016 14:33
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理--》档案核查管理--》核查结果明细查询
class CheckResultDetailPage(Page):

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()