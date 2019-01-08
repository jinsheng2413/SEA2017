# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: backgroupServeMonitor_page.py
@time: 2018/11/20 9:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统配置管理→后台服务监测
class BackgroupServeMonitorPage(Page):

    # 日期类型选择
    def inputChk_date_type_sel(self, tab_name):
        self.clickDt_Tab(tab_name, True, True)

    # 查询日期/从/到
    def inputDt_date(self, value):
        self.inputDate(value, True)

    # 运行状态
    def inputSel_operation_stat(self, option):
        self.selectDropDown(option, True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 系统管理→系统配置管理→后台服务监测→后台服务监测明细
class BackgroupServeMonitorDetailPage(Page):
    # JOB名称
    def inputStr_job_name(self, content):
        self.input(content)

    # 服务名称
    def inputStr_serve_name(self, content):
        self.input(content)

    # 日期类型选择
    def inputChk_date_type_sel(self, tab_name):
        self.clickDt_Tab(tab_name, True, True)

    # 查询日期/从/到
    def inputDt_date(self, value):
        self.inputDate(value, True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
