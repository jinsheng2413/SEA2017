# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: idCheckInfQuery_page.py
@time: 2018/11/15 11:34
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→权限密码管理→账号审核信息查询
class IdCheckInfQueryPage(Page):
    # 审核开始日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 审核结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 审核结果
    def inputSel_result(self, option):
        self.selectDropDown(option)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
