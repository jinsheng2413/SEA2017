# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→远程调试:终端调试工单统计
class TmnlInstallDetaiStatPage(Page):

    # 终端类型
    def inputSel_tmnl_type(self, options):
        self.selectDropDown(options)

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→终端管理→远程调试:终端调试
class TmnlInstallDetaiPage(Page):
    # --------------------------------------终端调试------------------------------------------
    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 申请单号
    def inputStr_app_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 终端厂家
    def inputSel_tmnl_factory(self, options):
        self.selectCheckBox(options, sleep_sec=2)


    # 终端类型
    def inputSel_tmnl_type(self, options):
        self.selectCheckBox(options, is_multi_tab=True, sleep_sec=2,
                            is_multi_elements=True)

    # 通信规约
    def inputSel_tmnl_protocol(self, options):
        self.selectCheckBox(options)

    # 表类型
    def inputSel_meter_type(self, options):
        self.selectDropDown(options)

    # 流程标识
    def inputSel_flow_id(self, options):
        self.selectDropDown(options)

    # 运行状态
    def inputSel_run_status(self, options):
        self.selectDropDown(options)

    # 装接类型
    def inputSel_mounting_type(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query(True)

    # 终端装接状态
    def inputChk_install_status(self, value):
        self.clickSingleCheckBox(value)

    # 查询状态
    def inputChk_query_type(self, value):
        self.clickRadioBox(value)
