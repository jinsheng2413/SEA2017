# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: collectTaskTemplate_page.py
@time: 2018/11/21 9:49
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.templateMan.collectTaskTemplate_locators import CollectTaskTemplateLocators


# 系统管理→模板管理→采集任务模板
class CollectTaskTemplatePage(Page):
    # 任务分类
    def inputSel_task_classify(self, index):
        self.click(*CollectTaskTemplateLocators.QRY_TASK_CLASSIFY)
        locator = self.get_select_locator(CollectTaskTemplateLocators.QRY_TASK_CLASSIFY_VALUE, index)
        self.click(*locator)

    # 任务类型
    def inputSel_task_type(self, index):
        self.click(*CollectTaskTemplateLocators.QRY_TASK_TYPE)
        locator = self.get_select_locator(CollectTaskTemplateLocators.QRY_TASK_TYPE_VALUE, index)
        self.click(*locator)

    # 模板名称
    def inputStr_template_name(self, content):
        self.input(content, *CollectTaskTemplateLocators.QRY_TEMPLATE_NAME)

    # 查询按钮
    def btn_search(self):
        self.click(*CollectTaskTemplateLocators.BTN_SEARCH)
