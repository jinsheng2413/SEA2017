# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: scriptCheckTaskSet_page.py
@time: 2018/11/19 0019 14:58
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→档案核查管理→脚本核查任务编制
class ScriptCheckTaskSetPage(Page):
    # 任务状态
    def inputSel_task_status(self, name):
        self.selectCheckBox(name)

    # 脚本名称
    def inputStr_script_name(self, value):
        self.input(value)

    # 脚本类型
    def inputSel_script_type(self, name):
        self.selectCheckBox(name)

    # 创建员工
    def inputStr_create_stall(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
