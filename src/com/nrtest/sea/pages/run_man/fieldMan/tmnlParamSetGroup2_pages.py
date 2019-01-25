# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: tmnlParamSetGroup2_pages.py
@time: 2018/11/8 0008 11:23
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→现场管理→终端抄表参数设置
class TermParaSetGroup2Page(Page):

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 终端规约
    def inputSel_tmnl_protocol(self, option):
        self.selectDropDown(option)

    # 下发状态
    def inputSel_send_status(self, option):
        self.selectDropDown(option)

    # 是否有f10下发失败的测量点
    def inputChk_f10_failsn(self, item):
        self.clickSingleCheckBox(item)

    # 查询
    def btn_qry(self):
        self.btn_query()
