# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: termParaSet_pages.py
@time: 2018/11/6 0006 10:36
@desc:
"""
from com.nrtest.common.base_page import Page


# 运行管理→现场管理→终端运行参数设置
class TermParaSetPage(Page):

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 终端厂商
    def inputSel_tmnl_factory(self, option):
        self.selectDropDown(option)

    # 规约
    def inputSel_tmnl_protocol(self, option):
        self.selectDropDown(option)

    # 任务状态
    def inputSel_task_status(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
