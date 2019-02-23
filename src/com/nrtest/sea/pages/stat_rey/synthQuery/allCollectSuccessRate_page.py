# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: allCollectSuccessRate_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class AllCollectSuccessRatePage(Page):
    # 电能表抄读状态
    def inputStr_meter_read_status(self, name):
        self.selectDropDown(name)

    # 终端运行状态
    def inputStr_tmnl_run_status(self, name):
        self.selectDropDown(name)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户类型
    def inputSel_cons_type(self, name):
        self.selectCheckBox(name)

    # 表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
