# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: flowAnaly_page.py
@time: 2018/11/9 0009 9:43
@desc:
"""

from com.nrtest.common.base_page import Page

from com.nrtest.sea.locators.run_man.simCardMan.runSituationCount.flowAnaly_locators import SIMFlowCountLocators


# 运行管理-->SIM卡管理-->运行情况分析-->流量分析
# 流量统计
class FlowStaticPage(Page):

    # 月份
    def inputStr_month(self, value):
        # self.input(value, *FlowCountLocators.QRY_MONTH)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(*FlowCountLocators.BTN_QRY)
        self.btn_query()


# 流量明细
class FlowDeatilPage(Page):

    # 月份
    def inputStr_month(self, value):
        # self.input(value, *FlowDetailLocators.QRY_MONTH)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(*FlowDetailLocators.BTN_QRY)
        self.btn_query(True)


# SIM卡超流量统计
class OverFlowStaticPage(Page):

    # 统计时间
    def inputStr_countTime(self, value):
        # self.input(value, *SIMFlowCountLocators.QRY_COUNT_TIME)
        self.inputDate(value)

    #SIM卡号
    def inputStr_simCardNo(self,value):
        # self.input(value,*SIMFlowCountLocators.QRY_SIM_NO)
        self.input(value)

    #终端地址
    def inputStr_tmnlAddr(self,value):
        # self.input(value,*SIMFlowCountLocators.QRY_TMNL_ADDR)
        self.input(value)

    # 日期类型
    def inputChk_data_method(self, option):
        self.clickRadioBox(option, True, True)

    # 是否超流量
    def inputChk_is_over_flow(self, items):
        self.clickCheckBox(items, SIMFlowCountLocators.QRY_IS_OVER_FLOW)

    # 查询
    def btn_qry(self):
        # self.click(*SIMFlowCountLocators.BTN_QRY)
        self.btn_query(True)
