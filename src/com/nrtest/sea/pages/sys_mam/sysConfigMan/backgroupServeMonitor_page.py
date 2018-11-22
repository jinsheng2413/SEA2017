# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: backgroupServeMonitor_page.py
@time: 2018/11/20 9:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.sysConfigMan.backgroupServeMonitor_locators import *


# 系统管理→系统配置管理→后台服务监测
class BackgroupServeMonitorPage(Page):
    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(BackgroupServeMonitorLocators.DATE_JS)
        self.input(content, *BackgroupServeMonitorLocators.QRY_DATE)

    # 运行状态
    def inputSel_operation_stat(self, index):
        self.click(*BackgroupServeMonitorLocators.QRY_OPERATION_STAT)
        locator = self.get_select_locator(BackgroupServeMonitorLocators.QRY_OPERATION_STAT_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*BackgroupServeMonitorLocators.BTN_SEARCH)


# 系统管理→系统配置管理→后台服务监测→后台服务监测明细
class BackgroupServeMonitorDetailPage(Page):
    # JOB名称
    def inputStr_job_name(self, index):
        self.input(index, *BackgroupServeMonitorDetailLocators.QRY_JOB_NAME)

    # 服务名称
    def inputStr_serve_name(self, index):
        self.input(index, *BackgroupServeMonitorDetailLocators.QRY_SERVE_NAME)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(BackgroupServeMonitorDetailLocators.DATE_JS)
        self.input(content, *BackgroupServeMonitorDetailLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*BackgroupServeMonitorDetailLocators.BTN_SEARCH)
