# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: TerminalDataQueryPage.py
@time: 2018/8/13 0002 14:00
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.terminalDataQuery_locators import TerminalDataQueryLocators


# 统计查询→综合查询→终端数据查询
class TerminalDataQueryPage(Page):
    # 页面元素
    # 终端资产号
    def inputStr_terminalnum(self, content):
        self.input(content, *TerminalDataQueryLocators.QRY_TERMINALNUM)

    # 终端地址
    def inputStr_terminaladdress(self, content):
        self.input(content, *TerminalDataQueryLocators.QRY_TERMINALADDRESS)

    # 查询按钮
    def btn_search(self):
        self.click(*TerminalDataQueryLocators.BTN_SEARCH)

    # 基本档案
    def btn_basicfile(self):
        self.click(*TerminalDataQueryLocators.BTN_BASICFILE)

    # 数据展示
    def btn_datashow(self):
        self.click(*TerminalDataQueryLocators.BTN_DATASHOW)

    # 操作对象选择区
    # 国网冀北电力有限公司
    def inputNode_jibei(self):
        self.click(*TerminalDataQueryLocators.TREE_JIBEI)

    # 唐山供电公司
    def inputNode_tangshan(self):
        self.click(*TerminalDataQueryLocators.TREE_TANGSHAN)

    # 直属用户
    def inputNode_directlyuser(self):
        self.click(*TerminalDataQueryLocators.TREE_DIRECTLYUSER)

    # 电网_国各庄
    def inputNode_guogezhuang(self):
        self.click(*TerminalDataQueryLocators.TREE_GUOGEZHUANG)

    # 数据展示→电量
    # 电量
    def btn_electricquantity(self):
        self.click(*TerminalDataQueryLocators.BTN_ELECTRICQUANTITY)

    # 总加组
    def sel_electricquantity_sumgroup(self):
        self.click(*TerminalDataQueryLocators.SEL_ELECTRICQUANTITY_SUMGROUP)

    # 查询日期_开始
    def inputDt_electricquantity_starttime(self, content):
        self.click(content, *TerminalDataQueryLocators.QRY_ELECTRICQUANTITY_STARTTIME)

    # 查询日期_结束
    def inputDt_electricquantity_endtime(self, content):
        self.click(content, *TerminalDataQueryLocators.QRY_ELECTRICQUANTITY_ENDTIME)

    # 查询按钮
    def btn_electricquantity_search(self):
        self.click(*TerminalDataQueryLocators.BTN_ELECTRICQUANTITY_SEARCH)

    # 数据展示→功率
    # 功率
    def btn_power(self):
        self.click(*TerminalDataQueryLocators.BTN_POWER)

    # 总加组
    def sel_power_sumgroup(self):
        self.click(*TerminalDataQueryLocators.SEL_POWER_SUMGROUP)

    # 查询日期
    def inputDt_power_time(self, content):
        self.click(content, *TerminalDataQueryLocators.QRY_POWER_TIME)

    # 查询按钮
    def btn_power_search(self):
        self.click(*TerminalDataQueryLocators.BTN_POWER_SEARCH)
