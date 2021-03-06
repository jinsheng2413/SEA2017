# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulInstallStat_page.py
@time: 2018/11/6 0006 11:27
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→采集信道管理→通信模块管理→通信模块安装统计
class CommModulInstallStatPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 模块类型
    def inputSel_module_type(self, options):
        self.selectDropDown(options)

    # 模块厂商
    def inputSel_module_factory(self, options):
        self.selectDropDown(options)

    # 模块版本
    def inputSel_module_ver(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
