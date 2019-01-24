# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→电表批量导出（冀北）
class ArchivesAutoReviewPage(Page):

    # 导入电表信息
    def inputSel_leadinto_meter(self, name):
        self.selectDropDown(name)

    # 时间
    def inputDt_stat_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
