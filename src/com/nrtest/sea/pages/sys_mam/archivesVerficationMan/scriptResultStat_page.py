# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: scriptResultStat_page.py
@time: 2018/11/20 0020 8:52
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→档案核查管理→脚本结果统计查询
class ScriptResultStatPage(Page):
    # 脚本名称
    def inputStr_script_name(self, value):
        self.input(value)  # , *ScriptResultDetailLocators.QRY_SCRIPT_NAME)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)  # , *ScriptResultDetailLocators.QRY_START_TIME)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)  # , *ScriptResultDetailLocators.QRY_END_TIME)

    # 查询
    def btn_qry(self):
        # self.click(ScriptResultDetailLocators.BTN_QRY)
        self.btn_query()
