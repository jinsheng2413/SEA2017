# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: taskTemplateSet_page.py
@time: 2018/11/20 0020 10:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→档案核查管理→档案核查模板编制
class TaskTemplateSetPage(Page):

    # 选择模板
    def inputSel_select_module(self, option):
        # self.click(TaskTemplateSetLocators.QRY_SELECT_MODULE)
        # locator = self.get_select_locator(TaskTemplateSetLocators.QRY_SELECT_MODULE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        # self.click(TaskTemplateSetLocators.BTN_QRY)
        self.btn_query()
