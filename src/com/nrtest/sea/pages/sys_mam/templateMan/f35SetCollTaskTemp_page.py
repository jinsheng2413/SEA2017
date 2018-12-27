# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: f35SetCollTaskTemp_page.py
@time: 2018/11/21 15:10
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→模板管理→F35设置采集任务模板
class F35SetCollTaskTempPage(Page):
    # 任务分类
    def inputSel_task_classify(self, option):
        # self.click(*F35SetCollTaskTempLocators.QRY_TASK_CLASSIFY)
        # locator = self.get_select_locator(F35SetCollTaskTempLocators.QRY_TASK_CLASSIFY_VALUE, option)
        # self.click(*locator)
        self.selectDropDown(option)

    # 任务类型
    def inputSel_task_type(self, option):
        # self.click(*F35SetCollTaskTempLocators.QRY_TASK_TYPE)
        # locator = self.get_select_locator(F35SetCollTaskTempLocators.QRY_TASK_TYPE_VALUE, option)
        # self.click(*locator)
        self.selectDropDown(option)

    # 模板名称
    def inputStr_template_name(self, content):
        # self.input(content, *F35SetCollTaskTempLocators.QRY_TEMPLATE_NAME)
        self.input(content)

    # 查询按钮
    def btn_search(self):
        # self.click(*F35SetCollTaskTempLocators.BTN_SEARCH)
        self.btn_query()
