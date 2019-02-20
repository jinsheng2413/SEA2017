# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: meter_state_arr_page.py
@time: 2019-02-20 09:32:14
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→费控管理→远程费控→新低压用户远程费控执行:低压用户费控列表
class NewRemoteCtrlExecu_low_sheet_Page(Page):
    # 催费控制批次号
    def inputStr_control_order_no(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 采集点编号
    def inputStr_cp_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_meter_asst_no(self, value):
        self.input(value)

    # 控制类别
    def inputSel_control_type(self, option):
        self.selectDropDown(option)

    # 工单状态
    def inputSel_app_status(self, option):
        self.selectDropDown(option)

    # 密文比对结果
    def inputSel_compare_result(self, option):
        self.selectDropDown(option)

    # 统计类型
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option, is_multi_elements=True, is_multi_tab=True)

    # 签发开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 签发结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 高级应用→费控管理→远程费控→新低压用户远程费控执行:低压用户费控汇总信息
class NewRemoteCtrlExecu_low_info_Page(Page):
    # 催费控制批次号
    def inputStr_control_order_no(self, value):
        self.curr_input(value, is_multi_elements=True, is_multi_tab=True)

    # 签发开始时间
    def inputDt_start_type(self, value):
        self.inputDate(value)

    # 签发结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 营销U1验签结果
    def inputSel_u1_result(self, option):
        self.selectDropDown(option)

    # 统计类型
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
