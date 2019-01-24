# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→抄表数据查询（冀北）：抄表明细
class RealDataPage(Page):
    # 曲线类型
    def inputChk_curve_type(self, index):
        self.clickRadioBox(index)

    # 终端生产厂家
    def inputSel_tmnl_factory(self, name):
        self.selectDropDown(name)

    # 反相采集结果
    def inputSel_reversCollectionResult(self, name):
        self.selectDropDown(name)

    # 终端运行状态
    def inputSel_tmnl_run_status(self, name):
        self.selectDropDown(name)

    # 电能表抄读状态
    def inputSel_meter_read_status(self, name):
        self.selectDropDown(name)

    # 数据类型
    def inputSel_data_type(self, name):
        self.selectDropDown(name)

    # 相位
    def inputSel_phase(self, name):
        self.selectDropDown(name)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 查询时间
    def inputDt_Time(self, value):
        self.inputDate(value)

    # 用户类型
    def inputSel_cons_type(self, name):
        self.selectCheckBox(name)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 统计查询→综合查询→抄表数据查询（冀北）：抄表失败明细
class RealDataFailDetailPage(Page):

    # 曲线类型
    def inputChk_curve_type(self, index):
        self.clickRadioBox(index, is_multi_elements=True, is_multi_tab=True)

    # 终端生产厂家
    def inputSel_tmnl_factory(self, name):
        self.selectDropDown(name)

    # 终端运行状态
    def inputSel_TmnlRunState(self, name):
        self.selectDropDown(name, is_multi_elements=True, is_multi_tab=True)

    # 电能表抄读状态
    def inputSel_meter_read_status(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 相位
    def inputSel_phase(self, name):
        self.selectDropDown(name, is_multi_elements=True, is_multi_tab=True)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 查询时间
    def inputDt_Time(self, value):
        self.inputDate(value)


    # 用户类型
    def inputSel_cons_type(self, name):
        self.selectCheckBox(name, is_multi_tab=True, is_multi_elements=True)

    # 反相采集结果
    def inputSel_revers_collection_result(self, name):
        self.selectDropDown(name)

    # 查询
    def btn_qry(self):
        self.btn_query(True)