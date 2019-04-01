# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulVersionMain_page.py
@time: 2018/11/6 0006 14:26
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→采集信道管理→通信模块管理→本地通信模块版本信息召测
class CommModulVersionMainPage(Page):
    # 终端类型
    def inputSel_tmnl_type(self, options):
        self.selectCheckBox(options)
        # self.selectDropDown(options)

    # 终端厂商
    def inputSel_tmnl_factory(self, options):
        self.selectDropDown(options)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 终端规约
    def inputSel_tmnl_protocol(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()