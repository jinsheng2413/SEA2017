# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: scriptResultDetail_page.py
@time: 2018/11/20 0020 8:52
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→档案核查管理→脚本结果明细查询
class ScriptResultDetailPage(Page):
    # 脚本名称
    def inputStr_scriptName(self, value):
        self.input(value)

    # 接收时间
    def inputDt_receive_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
