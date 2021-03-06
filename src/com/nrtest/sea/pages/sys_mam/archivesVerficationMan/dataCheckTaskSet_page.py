# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: dataCheckTaskSet_page.py
@time: 2018/11/19 0019 14:23
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.archivesVerficationMan.dataCheckTaskSet_locators import DataCheckTaskSetLocators


# 系统管理→档案核查管理→档案任务核查编制
class DataCheckTaskSetPage(Page):
    # 选择模板
    def inputChk_SelectDemo(self, option):
        self.selectDropDown(option)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 任务来源
    def inputSel_task_from(self, name):
        self.selectCheckBox(name)

    # 查询
    def btn_qry(self):
        self.click(DataCheckTaskSetLocators.BTN_QRY)
