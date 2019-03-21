# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: ReadCompleteRate_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量分析→采集完整率

class ReadCompleteRatePageNew(Page):
    # tab_name
    def inputChk_tab_name(self, value):
        self.clickTabPage(value)

    # 蕊片厂家
    def inputSel_chip_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_comm_mode(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_cons_type(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
