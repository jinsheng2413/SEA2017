# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: generalGroupSet_page.py
@time: 2018/11/12 15:14
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.groupMan.generalGroupSet_locators import GeneralGroupSetLocators



# 运行管理→群组管理→普通群组设置
class GeneralGroupSetPage(Page):
    # 群组分类
    def inputChk_group_type(self, option):
        self.clickRadioBox(option)
    # 名称
    def inputStr_name(self, content):
        # self.input(content, *GeneralGroupSetLocators.QRY_NAME)
        self.input(content)

    # 类别
    def inputChk_stats_type(self, option):
        self.clickRadioBox(option)

    # 有效日期
    def inputChk_valid_date(self, item):
        return self.clickSingleCheckBox(item, True, True, GeneralGroupSetLocators.QRY_VALID_DATE)

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
        # self.click(*GeneralGroupSetLocators.BTN_SEARCH)
        self.btn_query()
