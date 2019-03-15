# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: tgDate_page.py
@time: 2019-03-15 10:15:16
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→资料维护→台区资料维护(新)
class TgdataNewPage(Page):
    # 变电站
    def inputSel_subs(self, option):
        self.selectDropDown(option)

    # 线路
    def inputSel_line(self, option):
        self.selectDropDown(option)

    # 负责人
    def inputSel_master(self, option):
        self.selectDropDown(option)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 无负责人
    def inputChk_no_master(self, options):
        self.clickSingleCheckBox(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
