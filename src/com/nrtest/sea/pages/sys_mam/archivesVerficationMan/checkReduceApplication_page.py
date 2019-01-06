# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkReduceApplication_page.py
@time: 2018/11/20 0020 10:20
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理--》档案核查管理--》考核减免申请
class CheckReduceApplicationPage(Page):
    # 申请单号
    def inputStr_applyNo(self, value):
        self.input(value)  # , *CheckReduceApplicationLocators.QRY_APPLY_NO)

    # 接收时间
    def inputDt_start_time(self, value):
        # self.input(value, *CheckReduceApplicationLocators.QRY_START_TIME)
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        # self.input(value, *CheckReduceApplicationLocators.QRY_END_TIME)
        self.inputDate(value)
        # 查询

    def btn_qry(self):
        # self.click(CheckReduceApplicationLocators.BTN_QRY)
        self.btn_query()
