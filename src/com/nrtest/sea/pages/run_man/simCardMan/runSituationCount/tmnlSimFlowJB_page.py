# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: tmnlSimFlowJB_page.py
@time: 2018-11-12 10:03
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.simCardMan.runSituationCount.tmnlSimFlowJB_locators import TmnlSimFlowJB_1Locators, \
    TmnlSimFlowJB_2Locators


# 运行管理--SIM卡管理--运行情况分析--终端流量统计（冀北）
# 第一个tab页
class TmnlSimFlowJB_1Page(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *TmnlSimFlowJB_1Locators.QRY_TMNL_ADDR)

    # Sim卡号
    def inputStr_sim_no(self, value):
        self.input(value, *TmnlSimFlowJB_1Locators.QRY_SIM_NO)

    # 日期
    def inputStr_start_date(self, value):
        self.input(value, *TmnlSimFlowJB_1Locators.QRY_START_DATE)

    # 至 日期
    def inputStr_end_date(self, value):
        self.input(value, *TmnlSimFlowJB_1Locators.QRY_END_DATE)

    # 查询
    def btn_qry(self):
        self.click(*TmnlSimFlowJB_1Locators.BTN_QUERY)


# 第二个tab页
class TmnlSimFlowJB_2Page(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *TmnlSimFlowJB_2Locators.QRY_TMNL_ADDR)

    # Sim卡号
    def inputStr_sim_no(self, value):
        self.input(value, *TmnlSimFlowJB_2Locators.QRY_SIM_NO)

    # 日期
    def inputStr_date(self, value):
        self.input(value, *TmnlSimFlowJB_2Locators.QRY_DATE)

    # 查询
    def btn_qry(self):
        self.click(*TmnlSimFlowJB_2Locators.BTN_QUERY)
