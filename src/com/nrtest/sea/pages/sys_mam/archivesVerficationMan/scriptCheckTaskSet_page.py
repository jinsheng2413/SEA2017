# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: scriptCheckTaskSet_page.py
@time: 2018/11/19 0019 14:58
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.archivesVerficationMan.scriptCheckTaskSet_locators import \
    ScriptCheckTaskSetLocators


# 系统管理--》档案核查管理--》脚本核查任务编制
class ScriptCheckTaskSetPage(Page):
    # 任务状态
    def inputSel_taskStatus(self, name):
        # if name == '1':
        # self.clearInput(*ScriptCheckTaskSetLocators.QRY_TASK_STATUS)
        # else:
        # self.click(*ScriptCheckTaskSetLocators.QRY_TASK_STATUS)
        # locator = self.get_select_locator(ScriptCheckTaskSetLocators.QRY_TASK_STATUS_VALUE, name)
        # self.click(*locator)

        self.selectCheckBox(name)
    # 脚本名称
    def inputStr_scriptName(self, value):
        # self.input(value, *ScriptCheckTaskSetLocators.QRY_SCRIPT_NAME)

        self.input(value)

    # 脚本类型
    def inputSel_scriptType(self, name):
        # if name == '1':
        # self.clearInput(*ScriptCheckTaskSetLocators.QRY_SCRIPT_TYPE)
        # else:
        # self.click(*ScriptCheckTaskSetLocators.QRY_SCRIPT_TYPE)
        # locator = self.get_select_locator(ScriptCheckTaskSetLocators.QRY_SCRIPT_TYPE_VALUE, name)
        # self.click(*locator)

        self.selectCheckBox(name)
    # 创建员工
    def inputStr_creatStall(self, value):
        # self.input(value, *ScriptCheckTaskSetLocators.QRY_CREAT_STALL)

        self.input(value)

        # 查询

    def btn_qry(self):
        self.click(*ScriptCheckTaskSetLocators.BTN_QRY)
