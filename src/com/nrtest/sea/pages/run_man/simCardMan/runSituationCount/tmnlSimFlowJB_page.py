# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: tmnlSimFlowJB_page.py
@time: 2018-11-12 10:03
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→SIM卡管理→运行情况分析→终端流量统计（冀北）
# 第一个tab页
class TmnlSimFlowJB_1Page(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # Sim卡号
    def inputStr_sim_no(self, value):
        self.input(value)

    # 日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 至 日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 第二个tab页
class TmnlSimFlowJB_2Page(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        # self.input(value)
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # Sim卡号
    def inputStr_sim_no(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 流量状态
    def inputChk_flow_status(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
