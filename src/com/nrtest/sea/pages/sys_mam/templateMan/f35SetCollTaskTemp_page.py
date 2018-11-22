# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: f35SetCollTaskTemp_page.py
@time: 2018/11/21 15:10
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.templateMan.f35SetCollTaskTemp_locators import F35SetCollTaskTempLocators


# 系统管理→模板管理→F35设置采集任务模板
class F35SetCollTaskTempPage(Page):
    # 任务分类
    def inputSel_task_classify(self, index):
        self.click(*F35SetCollTaskTempLocators.QRY_TASK_CLASSIFY)
        locator = self.get_select_locator(F35SetCollTaskTempLocators.QRY_TASK_CLASSIFY_VALUE, index)
        self.click(*locator)

    # 任务类型
    def inputSel_task_type(self, index):
        self.click(*F35SetCollTaskTempLocators.QRY_TASK_TYPE)
        locator = self.get_select_locator(F35SetCollTaskTempLocators.QRY_TASK_TYPE_VALUE, index)
        self.click(*locator)

    # 模板名称
    def inputStr_template_name(self, content):
        self.input(content, *F35SetCollTaskTempLocators.QRY_TEMPLATE_NAME)

    # 查询按钮
    def btn_search(self):
        self.click(*F35SetCollTaskTempLocators.BTN_SEARCH)
