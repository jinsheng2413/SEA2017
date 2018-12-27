# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkResultStat_page.py
@time: 2018/11/19 0019 10:34
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.archivesVerficationMan.checkResultStat_locators import CheckResultStatLocators


# 系统管理--》档案核查管理--》核查结果统计查询
class CheckResultStatPage(Page):

    # 异常类型(下拉框还未有值)
    def inputSel_exceptionType(self, options):
        self.selectDropDown(options)

    # 台区编号
    def inputStr_zoneNO(self, value):
        self.inputDate(value)

    # 任务类型
    def inputSel_taskType(self, options):
        self.selectDropDown(options)

    # 开始时间
    def inputStr_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputStr_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
