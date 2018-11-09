# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: flowAnaly_page.py
@time: 2018/11/9 0009 9:43
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.simCardMan.runSituationCount.flowAnaly_locators import FlowCountLocators,FlowDetailLocators,SIMFlowCountLocators



# 运行管理-->SIM卡管理-->运行情况分析-->流量分析
class FlowCountPage(Page):

    # 月份
    def inputStr_month(self, value):
        self.input(value, *FlowCountLocators.QRY_MONTH)

        # 查询
    def btn_qry(self):
            self.click(*FlowCountLocators.BTN_QRY)



class FlowDeatilPage(Page):

    # 月份
    def inputStr_month(self, value):
        self.input(value, *FlowDetailLocators.QRY_MONTH)

    # 查询
    def btn_qry(self):
        self.click(*FlowDetailLocators.BTN_QRY)

class SIMFlowCountPage(Page):

    # 统计时间
    def inputStr_countTime(self, value):
        self.input(value, *SIMFlowCountLocators.QRY_COUNT_TIME)
    #SIM卡号
    def inputStr_simCardNo(self,value):
        self.input(value,*SIMFlowCountLocators.QRY_SIM_NO)
    #终端地址
    def inputStr_tmnlAddr(self,value):
        self.input(value,*SIMFlowCountLocators.QRY_TMNL_ADDR)

    # 查询
    def btn_qry(self):
        self.click(*SIMFlowCountLocators.BTN_QRY)