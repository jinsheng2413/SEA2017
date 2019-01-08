# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: databaseUpgradeStat_page.py
@time: 2018/11/15 15:44
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统配置管理→数据库升级情况
class DatabaseUpgradeStatPage(Page):
    # 升级日期
    def inputDt_upgrade_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
