# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: logEdit_page.py
@time: 2018/11/21 0021 13:46
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.logMan.logEdit_locators import LogEditLocators


# 系统管理--》日志管理--》值班日志
class LogEditPage(Page):
    # 值班人员工号
    def inputStr_dutyPersonNo(self, value):
        self.input(value, *LogEditLocators.QRY_DUTY_PERSON_NO)

    # 值班时间
    def inputStr_DutyTime(self, value):
        self.input(value, *LogEditLocators.QRY_DUTY_TIME)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *LogEditLocators.QRY_TO)

        # 查询

    def btn_qry(self):
        self.click(*LogEditLocators.BTN_QRY)
