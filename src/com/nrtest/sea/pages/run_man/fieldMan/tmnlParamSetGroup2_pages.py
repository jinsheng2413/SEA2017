# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: tmnlParamSetGroup2_pages.py
@time: 2018/11/8 0008 11:23
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.fieldMan.tmnlParamSetGroup2_locators import TermParaSetGroup2Locators


# 运行管理-现场管理-终端运行参数设置
class TermParaSetGroup2Page(Page):

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *TermParaSetGroup2Locators.QRY_TMNL_ADDR)

    # 终端规约
    def inputSel_tmnl_protory(self, index):
        self.click(*TermParaSetGroup2Locators.QRY_TMNL_PROTORY)
        locator = self.get_select_locator(TermParaSetGroup2Locators.QRY_TMNL_PROTORY_VALUE, index)
        self.click(*locator)

    # 下发状态
    def inputSel_task_status(self, index):
        self.click(*TermParaSetGroup2Locators.QRY_TAST_STATUS)
        locator = self.get_select_locator(TermParaSetGroup2Locators.QRY_TAST_STATUS_VALUE, index)
        self.click(*locator)

    # 查询
    def btn_qry(self):
        self.click(*TermParaSetGroup2Locators.BTN_QRY)
