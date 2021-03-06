# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: flowAnaly_page.py
@time: 2018/11/9 0009 9:43
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→SIM卡管理→运行情况分析→流量分析
# 流量统计
class FlowStaticPage(Page):

    # 月份
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()

# 流量明细
class FlowDeatilPage(Page):

    # 月份
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)

# SIM卡超流量统计
class OverFlowStaticPage(Page):

    # 统计时间
    def inputDt_static_time(self, value):
        self.inputDate(value)

    # SIM卡号
    def inputStr_sim_card_no(self,value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self,value):
        self.input(value)

    # 日期类型
    def inputChk_date_type(self, option):
        self.clickRadioBox(option)

    # 是否超流量
    def inputChk_over_flow_status(self, items):
        self.clickCheckBox_new(items, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
