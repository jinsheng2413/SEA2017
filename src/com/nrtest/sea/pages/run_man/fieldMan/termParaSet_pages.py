# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: termParaSet_pages.py
@time: 2018/11/6 0006 10:36
@desc:
"""
from com.nrtest.common.base_page import Page


# 运行管理-现场管理-终端运行参数设置
class TermParaSetPage(Page):

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        # self.input(value, *TermParaSetLocators.QRY_TMNL_ADDR)
        self.input(content)

    # 终端厂商
    def inputSel_tmnl_factory(self, option):
        # self.click(*TermParaSetLocators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(TermParaSetLocators.QRY_TMNL_FACTORY_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(option)

    # 规约
    def inputSel_tmnl_protory(self, option):
        # self.click(*TermParaSetLocators.QRY_TMNL_PROTORY)
        # locator = self.get_select_locator(TermParaSetLocators.QRY_TMNL_PROTORY_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(option)

    # 任务状态
    def inputSel_task_status(self, option):
        # self.click(*TermParaSetLocators.QRY_TAST_STATUS)
        # locator = self.get_select_locator(TermParaSetLocators.QRY_TAST_STATUS_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        # self.click(*TermParaSetLocators.BTN_QRY)
        self.btn_query()
