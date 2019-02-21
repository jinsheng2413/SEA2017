# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: logEdit_page.py
@time: 2018/11/21 0021 13:46
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→日志管理→值班日志
class LogEditPage(Page):
    # 值班人员工号
    def inputStr_duty_person_no(self, value):
         self.input(value)

    # 值班时间
    def inputDt_start_time(self, value):
          self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()