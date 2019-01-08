# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: msgSet_page.py
@time: 2018/11/27 9:59
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→信息定制→推送信息定制→信息设置
class MsgSetPage(Page):
    # 重要性级别
    def inputSel_importance_level(self, option):
        self.selectDropDown(option)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
