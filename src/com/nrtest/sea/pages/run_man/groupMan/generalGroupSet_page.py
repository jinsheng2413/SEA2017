# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: generalGroupSet_page.py
@time: 2018/11/12 15:14
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→群组管理→普通群组设置
class GeneralGroupSetPage(Page):
    # 群组分类
    def inputChk_group_deal(self, option):
        self.clickRadioBox(option)
    # 名称
    def inputStr_group_name(self, content):
        self.input(content)

    # 类别
    def inputChk_group_type(self, option):
        self.clickRadioBox(option)

    # 有效日期
    def inputChk_valid_date(self, item):
        return self.clickSingleCheckBox(item)  # , True, True, GeneralGroupSetLocators.QRY_VALID_DATE)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
