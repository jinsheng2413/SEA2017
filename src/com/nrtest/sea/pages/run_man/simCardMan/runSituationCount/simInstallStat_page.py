# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: simInstallStat_page.py
@time: 2018/11/9 0009 9:14
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→SIM卡管理→运行情况分析→安装情况统计
# 安装情况统计
class SimInstallStatPageStatic(Page):

    # 运营商
    def inputSel_operator(self, item):
        self.selectDropDown(item)

    # 查询
    def btn_qry(self):
        self.btn_query()

# 安装情况明细
class SimInstallStatPageDetail(Page):

    # 运营商
    def inputSel_operator(self, item):
        self.selectDropDown(item, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
