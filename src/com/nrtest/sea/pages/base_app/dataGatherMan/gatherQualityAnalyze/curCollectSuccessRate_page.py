# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: curCollectSuccessRate_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量分析→实时采集成功率:实时采集成功率
class CurCollectSuccessRatePage(Page):

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value, True)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value, True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→数据采集管理→采集质量分析→实时采集成功率:实时采集成功率统计
class CurCollectSuccessRate_count_Page(Page):
    # 日期时间
    def inputDt_date_time(self, value):
        self.inputDate(value)

    # 统计查询
    def btn_count_qry(self):
        self.btn_query(True)


# 基本应用→数据采集管理→采集质量分析→实时采集成功率:实时采集失败明细
class CurCollectSuccessRate_detail_Page(Page):
    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 日期时间
    def inputDt_date_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
