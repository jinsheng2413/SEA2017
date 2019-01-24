# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→档案变更记录
class ArchivesChangeRecordPage(Page):
    # 设备类型
    def inputSel_device_type(self, name):
        self.selectDropDown(name)

    # 变更类型
    def inputSel_change_type(self, name):
        self.selectDropDown(name)

    # 接收时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 用户类型
    def inputChk_cons_type(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
