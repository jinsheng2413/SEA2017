# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysOtherQuery_page.py
@time: 2018/11/8 11:07
@desc:
"""
from com.nrtest.common.base_page import Page


# 统计查询→报表管理→国网报表→系统其他运行指标

class SysOtherQueryPage(Page):

    # 统计分类
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 查询日期

    def inputDt_query_dateS(self, value):
        self.inputDate(value)  # , *SysOtherQueryLocators.QRY_DATE)

    # 统计口径
    def inputSel_stat_scope(self, option):
        # self.click(SysOtherQueryLocators.QRY_STAT_SCOPE)
        # locator = self.get_select_locator(SysOtherQueryLocators.QRY_STAT_SCOPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        # self.click(SysOtherQueryLocators.BTN_QRY)
        self.btn_query()
