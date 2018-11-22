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


#系统管理--》档案核查管理--》核查结果统计查询
class CheckResultStatPage(Page):

    # 异常类型(下拉框还未有值)
    def inputSel_exceptionType(self, name):
        self.click(*CheckResultStatLocators.QRY_EXCEPTION_TYPE)
        locator = self.get_select_locator(CheckResultStatLocators.QRY_EXCEPTION_TYPE, name)
        self.click(*locator)

    # 台区编号
    def inputStr_zoneNO(self, value):
        self.input(value, *CheckResultStatLocators.QRY_ZONE_AREA_NO)

    # 任务类型
    def inputSel_taskType(self, name):
        self.click(*CheckResultStatLocators.QRY_TASK_TYPE)
        locator = self.get_select_locator(CheckResultStatLocators.QRY_TASK_TYPE_VALUE, name)
        self.click(*locator)
        self.click(*CheckResultStatLocators.QRY_TASK_TYPE)

    # 开始时间
    def inputStr_start_time(self, value):
        self.input(value, *CheckResultStatLocators.QRY_START_TIME)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *CheckResultStatLocators.QRY_END_TIME)

        # 查询
    def btn_qry(self):
            self.click(*CheckResultStatLocators.BTN_QRY)