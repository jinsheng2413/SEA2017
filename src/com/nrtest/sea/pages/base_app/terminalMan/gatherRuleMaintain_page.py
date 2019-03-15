# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: gather_rule_maintain.py
@time: 2019-03-14 19:38:57
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→采集规则维护
class GatherRuleMaintainPage(Page):
    # 查询
    def btn_qry(self):
        self.btn_query()
