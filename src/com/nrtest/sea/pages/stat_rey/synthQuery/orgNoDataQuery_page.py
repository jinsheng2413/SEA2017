# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: orgNoDataQuery_page.py
@time: 2018/9/29 15:36
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.orgNoDataQuery_locators import OrgNoDataQueryLocator


# 统计查询→综合查询→供电单位数据查询
class OrgNoDataPage(Page):
    # 日期
    def inputDt_date(self, content):
        self.exec_script(OrgNoDataQueryLocator.DATE_JS)
        self.input(content, *OrgNoDataQueryLocator.DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*OrgNoDataQueryLocator.BTN_SEARCH)
