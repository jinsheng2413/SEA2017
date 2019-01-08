# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userOperationMan_page.py
@time: 2018/11/20 14:57
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统配置管理→用户操作监测
class UserOperationMonitorPage(Page):
    # 日期
    def inputDt_stat_date(self, content):
        self.inputDate(content)

    # 操作模块
    def inputSel_operation_module(self, option):
        self.selectDropDown(option)

    # 操作人员
    def inputStr_operator(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
