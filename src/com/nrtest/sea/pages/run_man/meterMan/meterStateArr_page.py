# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: meterStateArr_page.py
@time: 2019-02-19 08:55:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→电能表管理→电能表状态维护(蒙东)
class MeterStateArrPage(Page):
    # 终端状态
    def inputSel_tmnl_status(self, option):
        self.selectDropDown(option)

    # 终端类型
    def inputSel_tmnl_type(self, option):
        self.selectDropDown(option)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 包含下级供电单位
    def inputChk_contain_org(self, options):
        self.clickCheckBox_new(options)

    # 查询
    def btn_qry(self):
        self.btn_query(True, idx=1)
