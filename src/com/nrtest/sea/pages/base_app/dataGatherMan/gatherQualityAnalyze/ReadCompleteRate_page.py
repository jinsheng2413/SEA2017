# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量分析→采集完整率:采集完整率
class ReadCompleteRatePage(Page):
    # 蕊片厂家
    def inputSel_chip_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_commu_mode(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_cons_sort(self, name):
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


# 基本应用→数据采集管理→采集质量分析→采集完整率:采集完整率统计
class ReadCompleteRate_count_Page(Page):
    # 日期时间
    def inputDt_date_time_count(self, value):
        self.inputDate(value)

    # 用户类型
    def inputSel_cons_sort(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_comm_mode(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    #  蕊片厂家
    def inputSel_chip_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→数据采集管理→采集质量分析→采集完整率:采集完整率明细
class ReadCompleteRate_detail_Page(Page):
    # 用户类型
    def inputSel_cons_sort(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_comm_mode(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    #  蕊片厂家
    def inputSel_chip_factory(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

        # 日期时间

    def inputDt_date_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
