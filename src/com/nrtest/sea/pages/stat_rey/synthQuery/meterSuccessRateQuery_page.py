# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterSuccessRateQuery_page.py
@time: 2018/10/10 14:48
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→抄表成功率查询（河北）
# 按地区、厂家统计
class MeterSuccessRateQueryPage(Page):
    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.clean_label(index)
        self.selectCheckBox(index)

    # 通信方式
    def inputSel_comm_mode(self, index):
        self.selectCheckBox(index)

    # 规约类型
    def inputSel_protocol_type(self, index):
        self.selectCheckBox(index)

    # 用户范围
    def inputSel_cons_range(self, index):
        self.selectDropDown(index)

    # 统计类型
    def inputSel_stat_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 按时间统计
class MeterSuccessRateQueryTimePage(Page):
    # 开始时间
    def inputDt_start_date(self, index):
        self.inputDate(index)

    # 结束时间
    def inputDt_end_date(self, index):
        self.inputDate(index)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index, is_multi_elements=True, is_multi_tab=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.clean_label(index)
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_comm_mode(self, index):
        self.selectCheckBox(index, is_multi_elements=True, is_multi_tab=True)

    # 规约类型
    def inputSel_protocol_type(self, index):
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 用户范围
    def inputSel_cons_range(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 按华北要求统计
class MeterSuccessRateQueryHuaBeiPage(Page):
    # 开始时间
    def inputDt_start_date(self, index):
        self.inputDate(index)

    # 结束时间
    def inputDt_end_date(self, index):
        self.inputDate(index)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index, is_multi_elements=True, is_multi_tab=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.clean_label(index)
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_comm_mode(self, index):
        self.selectCheckBox(index, is_multi_elements=True, is_multi_tab=True)

    # 规约类型
    def inputSel_protocol_type(self, index):
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 连续抄表失败明细
class MeterSuccessRateQueryFailedPage(Page):
    # 日期
    def inputDt_query_date(self, index):
        self.inputDate(index)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index, is_multi_elements=True, is_multi_tab=True)

    # 运行状态
    def inputSel_run_status(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 接线方式
    def inputSel_conn_way(self, index):
        self.selectDropDown(index)

    # 用户编号
    def inputStr_cons_no(self, index):
        self.input(index)

    # 终端地址
    def inputStr_tmnl_addr(self, index):
        self.input(index)

    # 农排用户选择
    def inputSel_user_select(self, index):
        self.selectDropDown(index)

    # 连续失败天数
    def inputStr_read_fail_days_start(self, index):
        self.input(index)

    # 到
    def inputStr_read_fail_days_end(self, index):
        self.input(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
