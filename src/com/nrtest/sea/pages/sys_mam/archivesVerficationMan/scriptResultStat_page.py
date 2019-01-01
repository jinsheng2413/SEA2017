# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: scriptResultDetail_page.py
@time: 2018/11/20 0020 8:52
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.archivesVerficationMan.scriptResultDetail_locators import \
    ScriptResultDetailLocators


# 系统管理--》档案核查管理--》脚本结果统计查询
class scriptResultStatPage(Page):
    # 脚本名称
    def inputStr_scriptName(self, value):
        self.input(value, *ScriptResultDetailLocators.QRY_SCRIPT_NAME)

    # 接收时间
    def inputStr_receive_time(self, value):
        self.input(value, *ScriptResultDetailLocators.QRY_START_TIME)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *ScriptResultDetailLocators.QRY_END_TIME)

        # 查询

    def btn_qry(self):
        self.click(ScriptResultDetailLocators.BTN_QRY)
