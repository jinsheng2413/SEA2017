# -*- coding:utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysRunContrastQuery_page.py
@time: 2018/11/6 15:24
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.reportMan.stateGridReport.sysRunContrastQuery_locators import \
    SysRunContrastQueryLocators


# 统计查询--》报表管理--》国网报表--》采集系统运行指标
class SysRunContrastQueryPage(Page):
    # 查询
    def btn_qry(self):
        self.click(*SysRunContrastQueryLocators.BTN_QRY)
