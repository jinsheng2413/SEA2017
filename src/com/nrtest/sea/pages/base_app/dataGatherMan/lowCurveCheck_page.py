# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: ReadCompleteRate_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量检查(new)→低压采集质量检查

class LowCurveCheckPage(Page):
    # 统计方式
    def inputChk_stat_type(self, value):
        self.clickRadioBox(value)

    # 通信方式
    def inputSel_comm_type(self, value):
        self.selectDropDown(value)

    # 抄表日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 运行状态
    def inputSel_run_status(self, value):
        self.selectDropDown(value)

    # 当天抄读成功率
    def inputSel_read_success(self, value):
        self.selectDropDown(value)

    # 终端厂商
    def inputSel_tmnl_factory(self, value):
        self.selectDropDown(value)

    # 规约类型
    def inputSel_protocol_type(self, value):
        self.selectDropDown(value)

    # 终端类型
    def inputSel_tmnl_type(self, value):
        self.selectDropDown(value)

    # 百分比
    def inputStr_no_label_input(self, value):
        self.noLabelInput(value)

    # 查询
    def btn_query(self):
        self.btn_query(True)
