# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: changeCTPT_page.py
@time: 2019-03-13 10:22
@desc:
"""

from com.nrtest.common.base_page import Page

# 业务变更→换CT/PT:换CTPT操作
class ChangeCTPTOperatePage(Page):
    # 更换时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 提交按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)


# 业务变更→换CT/PT:换CTPT记录
class ChangeCTPTRecordPage(Page):
    # 时间类型
    def inputChk_date_type(self, value):
        self.selectDropDown(value)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 提交按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
