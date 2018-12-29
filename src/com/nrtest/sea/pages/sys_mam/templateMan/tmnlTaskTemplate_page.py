# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlTaskTemplate_page.py
@time: 2018/11/21 14:38
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→模板管理→终端任务模板
class TmnlTaskTemplatePage(Page):
    # 任务状态
    def inputSel_task_stat(self, option):
        # self.click(*TmnlTaskTemplateLocators.QRY_TASK_STAT)
        # locator = self.get_select_locator(TmnlTaskTemplateLocators.QRY_TASK_STAT_VALUE, option)
        # self.click(*locator)
        self.selectDropDown(option)

    # 方案类型
    def inputSel_scheme_type(self, option):
        # self.click(*TmnlTaskTemplateLocators.QRY_SCHEME_TYPE)
        # locator = self.get_select_locator(TmnlTaskTemplateLocators.QRY_SCHEME_TYPE_VALUE, option)
        # self.click(*locator)
        self.selectDropDown(option)

    # 执行优先级
    def inputSel_execution_priority(self, option):
        # self.click(*TmnlTaskTemplateLocators.QRY_EXECUTION_PRIORITY)
        # locator = self.get_select_locator(TmnlTaskTemplateLocators.QRY_EXECUTION_PRIORITY_VALUE, option)
        # self.click(*locator)
        self.selectDropDown(option)

    # 启用开始时间
    def inputChk_use_startdate(self, item):
        return self.clickSingleCheckBox(item, True, True)

    # 启用结束时间
    def inputChk_use_enddate(self, item):
        return self.clickSingleCheckBox(item, True, True)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        # self.exec_script(GeneralGroupSetLocators.START_DATE_JS)
        # self.input(content) #, *GeneralGroupSetLocators.QRY_START_DATE)
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        # self.exec_script(GeneralGroupSetLocators.END_DATE_JS)
        # self.input(content, *GeneralGroupSetLocators.QRY_END_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(*TmnlTaskTemplateLocators.BTN_SEARCH)
        self.btn_query()
