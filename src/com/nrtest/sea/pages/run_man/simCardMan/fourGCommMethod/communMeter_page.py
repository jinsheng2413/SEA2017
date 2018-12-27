# -*- coding:utf-8 -*-


"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: flowAnaly_page.py
@time: 2018/12/27 0009 9:43
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理-->SIM卡管理-->4G通信方式-->抄表情况
class CommumMeterPage(Page):

    # 月份
    def inputStr_month(self, value):
        # self.input(value, *FlowCountLocators.QRY_MONTH)
        self.input(value)

        # 查询
    def btn_qry(self):
        # self.click(*FlowCountLocators.BTN_QRY)
        self.btn_query()


# 流量明细
class FlowDeatilPage(Page):

    # 月份
    def inputStr_month(self, value):
        # self.input(value, *FlowDetailLocators.QRY_MONTH)
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
