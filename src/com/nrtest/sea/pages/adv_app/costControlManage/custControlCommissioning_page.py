# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: custControlCommissioning_page.py
@time: 2018/8/23 0023 10:57
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→费控管理→本地费控→费控投入调试
class CustControlCommissioning_page(Page):
    # 电量下发成功自动发送短信
    def inputChk_auto_send_sms(self, value):
        self.clickCheckBox_new(value)

    # 控制类型
    def inputChk_ctrl_type(self, name):
        self.clickRadioBox(name)

    # 营销单号
    def inputStr_app_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)
    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 按
    def inputSel_debug_date_type(self, option):
        self.selectDropDown(option)

    # 下发状态
    def inputSel_send_status(self, option):
        self.selectDropDown(option)

    # 点击查询按钮
    def btn_qry(self):
        self.btn_query()

