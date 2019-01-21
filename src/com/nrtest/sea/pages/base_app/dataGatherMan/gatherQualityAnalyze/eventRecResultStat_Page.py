# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量分析→事件记录结果统计
class EventRecResultStatPage(Page):

    # 开始时间
    def inputDt_start_time(self, content):
        self.inputDate(content)

    # 结束时间
    def inputDt_end_time(self, content):
        self.inputDate(content)

    # 事件类型
    def inputSel_event_type(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
