# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkReducePool_page.py
@time: 2018/11/20 0020 10:47
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.archivesVerficationMan.checkReducePool_locators import CheckReducePoolLocators


# 系统管理--》档案核查管理--》考核减免汇总
class CheckReducePoolPage(Page):
    # 申请单号
    def inputStr_apply_no(self, value):
        self.input(value)

    # 工单状态
    def inputSel_work_status(self, options):
        self.selectDropDown(options)

    # 申请时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
