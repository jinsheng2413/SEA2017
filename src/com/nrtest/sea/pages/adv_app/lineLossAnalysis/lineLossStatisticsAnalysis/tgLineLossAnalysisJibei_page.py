# -*- coding: utf-8 -*-"""@author: 韩笑@license: (C) Copyright 2018, Nari.@file: tgLineLossAnalysisJibei_page.py@time: 2018/10/31 16:23@desc:"""from com.nrtest.common.base_page import Page# 高级应用→线损分析→线损统计分析→台区线损分析（冀北）class TgLineLossAnalysisJibeiPage(Page):    # 台区编号    def inputStr_tg_no(self, content):        self.input(content)    # 台区名称    def inputStr_tg_name(self, content):        self.input(content)    # 安装率    def inputSel_installation_rate(self, index):        self.clean_label(index)        self.selectDropDown(index)    def inputStr_installation_rate(self, content):        self.input(content)    # 抄读成功率    def inputSel_read_success_rate(self, index):        self.clean_label(index)        self.selectDropDown(index)    def inputStr_read_success_rate(self, content):        self.input(content)    # 线损率    def inputSel_line_loss_rate(self, index):        self.clean_label(index)        self.selectDropDown(index)    def inputStr_line_loss_rate(self, content):        self.input(content)    # 查询日期    def inputDt_query_date(self, content):        self.inputDate(content)    # 时间统计类型    def inputDTTAB_statDateType(self, name):        self.clickDt_Tab(name)    # 可算    def inputChk_may(self, name):        self.clickRadioBox(name)    # 达标    def inputChk_reach(self, name):        self.clickRadioBox(name)    # 查询按钮    def btn_search(self):        self.btn_query()