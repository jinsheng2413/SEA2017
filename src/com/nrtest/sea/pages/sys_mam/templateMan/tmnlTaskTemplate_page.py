# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlTaskTemplate_page.py
@time: 2018/11/21 14:38
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.templateMan.tmnlTaskTemplate_locators import TmnlTaskTemplateLocators


# 系统管理→模板管理→终端任务模板
class TmnlTaskTemplatePage(Page):
    # 任务状态
    def inputSel_task_stat(self, index):
        self.click(*TmnlTaskTemplateLocators.QRY_TASK_STAT)
        locator = self.get_select_locator(TmnlTaskTemplateLocators.QRY_TASK_STAT_VALUE, index)
        self.click(*locator)

    # 方案类型
    def inputSel_scheme_type(self, index):
        self.click(*TmnlTaskTemplateLocators.QRY_SCHEME_TYPE)
        locator = self.get_select_locator(TmnlTaskTemplateLocators.QRY_SCHEME_TYPE_VALUE, index)
        self.click(*locator)

    # 执行优先级
    def inputSel_execution_priority(self, index):
        self.click(*TmnlTaskTemplateLocators.QRY_EXECUTION_PRIORITY)
        locator = self.get_select_locator(TmnlTaskTemplateLocators.QRY_EXECUTION_PRIORITY_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*TmnlTaskTemplateLocators.BTN_SEARCH)